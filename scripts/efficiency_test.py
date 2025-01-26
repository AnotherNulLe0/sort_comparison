from .utils import repeat, mem_repeat, get_percent_template, calc_percent
from .cfg import ARRAY_LENGTH, SORT_REPEATS, STEP, SORTING_FUNCTIONS
from random import randint
from time import time
from multiprocessing import Process, Value

def get_efficiency(is_sorted, global_counter, sorting_functions, array_length, sort_repeats, step):
    efficiency = {}
    for function in sorting_functions:
        efficiency[function.__name__] = [[], []]

    for length in range(step, array_length+step, step):
        if is_sorted:
            input_data = [i+1 for i in range(length)]
        else:
            input_data = [randint(1, length) for i in range(length)]

        for function in sorting_functions:
            try:
                efficiency[function.__name__][0].append(repeat(lambda: function(input_data), sort_repeats))
                efficiency[function.__name__][1].append(length)
            except RecursionError:
                pass
            global_counter.value += 1
            # print_percent(global_counter.value, len(sorting_functions), array_length, step)
    # print(f"{'sorted' if is_sorted else 'unsorted'} FINISHED")
    
    return efficiency

def get_memory(is_sorted, global_counter, sorting_functions, array_length, sort_repeats, step):
    efficiency = {}
    for function in sorting_functions:
        efficiency[function.__name__] = [[], []]

    for length in range(step, array_length+step, step):
        if is_sorted:
            input_data = [i+1 for i in range(length)]
        else:
            input_data = [randint(1, length) for i in range(length)]

        for function in sorting_functions:
            try:
                # result =
                efficiency[function.__name__][0].append(mem_repeat(lambda: function(input_data), sort_repeats))
                efficiency[function.__name__][1].append(length)
            except RecursionError:
                pass
            global_counter.value += 1
            # print_percent(global_counter.value, len(sorting_functions), array_length, step)
    # print(f"{'sorted' if is_sorted else 'unsorted'} FINISHED")
    
    return efficiency

# def setup(queue, is_sorted, SORTING_FUNCTIONS, ARRAY_LENGTH, SORT_REPEATS, STEP):
def setup(queue, is_sorted, global_counter, sorting_functions, array_length, sort_repeats, step):
    efficiency = get_efficiency(is_sorted, global_counter, sorting_functions, array_length, sort_repeats, step)
    queue.put(efficiency)
    # print(f"\n{is_sorted} IS DONE")

def count_time(counter, flag, total, arrlen, step):
    start = time()
    while flag.value != 1:
        cur_progress = get_percent_template().format(calc_percent(counter.value, total, arrlen, step)) + f", прошло {time()-start:.1f}с"
        print(cur_progress, end="")

def run(array_length, sort_repeats, step, sorting_functions, unsorted_efficiency=None, sorted_efficiency=None, unsorted_memory=None, sorted_memory=None):
    counter = Value('I', 0)
    flag = Value('B', 0)
    time_counting = Process(target=count_time, args=(counter, flag, len(sorting_functions), array_length, step))
    start = time()
    time_counting.start()
    if not unsorted_memory:
        unsorted_memory =  get_memory(False, counter, sorting_functions, array_length, sort_repeats, step)
    if not sorted_memory:
        sorted_memory =  get_memory(True, counter, sorting_functions, array_length, sort_repeats, step)
    if not unsorted_efficiency:
        unsorted_efficiency =  get_efficiency(False, counter, sorting_functions, array_length, sort_repeats, step)
    if not sorted_efficiency:
        sorted_efficiency =  get_efficiency(True, counter, sorting_functions, array_length, sort_repeats, step)
    flag.value = 1
    cur_progress = get_percent_template().format(calc_percent(counter.value, len(sorting_functions), array_length, step)) + f", прошло {time()-start:.1f}с"
    print(cur_progress)
    return (sorted_efficiency, unsorted_efficiency, sorted_memory, unsorted_memory)

if __name__ == "__main__":
    run(ARRAY_LENGTH, SORT_REPEATS, STEP, SORTING_FUNCTIONS)