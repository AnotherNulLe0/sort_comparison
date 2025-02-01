from .utils import repeat, get_percent_template, calc_percent
from .cfg import ARRAY_LENGTH, SORT_REPEATS, STEP, SORTING_FUNCTIONS
from random import randint
from time import time
from multiprocessing import Process, Value
from tracemalloc import start as trace_start
from tracemalloc import stop as trace_stop
from tracemalloc import get_traced_memory

def get_efficiency(is_sorted, global_counter, sorting_functions, array_length, sort_repeats, step):
    efficiency = {}
    mem_efficiency = {}

    # Создаётся два словаря
    # ключ - имя сортировочного алгоритма
    # значение - 2 списка, первый список хранит результаты тестов, а второй хранит данные о том, какая длина массива была в соответствующем тесте 
    for function in sorting_functions:
        efficiency[function.__name__] = [[], []]
        mem_efficiency[function.__name__] = [[], []]

    # Выполняет сортировку sort_repeats раз, с увеличением длинны массива от step до array_length (включительно) с шагом step
    for length in range(step, array_length+step, step):

        # В зависимости от тест будет передаваться либо хаотичный, либо отсортированный массив
        if is_sorted:
            input_data = [i+1 for i in range(length)]
        else:
            input_data = [randint(1, length) for i in range(length)]

        # Тестирует каждую функцию, указанную в cfg.py
        for function in sorting_functions:
            # Начинает отслеживать потребляемую память
            trace_start()
            try:
                efficiency[function.__name__][0].append(repeat(lambda: function(input_data), sort_repeats))
                efficiency[function.__name__][1].append(length)
            except RecursionError: # Быстрая сортировка может уходить в бесконечную рекурсию
                pass
            mem_efficiency[function.__name__][0].append(get_traced_memory()[1]) # Записывает потребляемую память алгоритма
            mem_efficiency[function.__name__][1].append(length)
            trace_stop()
            global_counter.value += 1
    
    return (efficiency, mem_efficiency)

def count_time(counter, flag, total, arrlen, step):
    start = time()
    while flag.value != 1:
        cur_progress = get_percent_template().format(calc_percent(counter.value, total, arrlen, step)) + f", прошло {time()-start:.1f}с"
        print(cur_progress, end="")
    cur_progress = get_percent_template().format(calc_percent(counter.value, total, arrlen, step)) + f", прошло {time()-start:.1f}с"
    print(cur_progress, end="")

def run(array_length, sort_repeats, step, sorting_functions):
    unsorted_efficiency, sorted_efficiency, unsorted_memory, sorted_memory = (None,) * 4
    counter = Value('I', 0)
    flag = Value('B', 0)
    time_counting = Process(target=count_time, args=(counter, flag, len(sorting_functions), array_length, step))
    time_counting.start()

    unsorted_efficiency, unsorted_memory =  get_efficiency(False, counter, sorting_functions, array_length, sort_repeats, step)
    sorted_efficiency, sorted_memory =  get_efficiency(True, counter, sorting_functions, array_length, sort_repeats, step)

    flag.value = 1

    return (sorted_efficiency, unsorted_efficiency, sorted_memory, unsorted_memory)

if __name__ == "__main__":
    run(ARRAY_LENGTH, SORT_REPEATS, STEP, SORTING_FUNCTIONS)