from utils import *
from graph_draw import *
from random import randint
from time import time

def get_efficiency(is_sorted, global_counter, sorting_functions, array_length, sort_repeats, step):
    efficiency = {}
    for function in sorting_functions:
        efficiency[function.__name__] = [[], []]

    for length in range(step, array_length, step):
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
            print(f"\rЗавершено на {global_counter.value*100/(2*len(sorting_functions)*((array_length-step)/step)):.2f}%", end="")
    # print(f"{'sorted' if is_sorted else 'unsorted'} FINISHED")
    
    return efficiency

# def setup(queue, is_sorted, SORTING_FUNCTIONS, ARRAY_LENGTH, SORT_REPEATS, STEP):
def setup(queue, is_sorted, global_counter, sorting_functions, array_length, sort_repeats, step):
    efficiency = get_efficiency(is_sorted, global_counter, sorting_functions, array_length, sort_repeats, step)
    queue.put(efficiency)
    # print(f"\n{is_sorted} IS DONE")

def run(array_length, sort_repeats, step, sorting_functions, unsorted_efficiency=None, sorted_efficiency=None):
    start = time()
    class Counter:
        def __init__(self):
            self.value = 0
    counter = Counter()
    if not unsorted_efficiency:
        unsorted_efficiency =  get_efficiency(False, counter, sorting_functions, array_length, sort_repeats, step)
    if not sorted_efficiency:       
        sorted_efficiency =  get_efficiency(True, counter, sorting_functions, array_length, sort_repeats, step)
    print()
    return (sorted_efficiency, unsorted_efficiency)

if __name__ == "__main__":
    run(ARRAY_LENGTH, SORT_REPEATS, STEP, SORTING_FUNCTIONS)