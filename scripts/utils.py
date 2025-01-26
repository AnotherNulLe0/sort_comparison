from time import time
from tracemalloc import start, stop, get_traced_memory

def promt(text):
    print(text)
    result = True
    while result != "n" and result != "y":
        print("Вы уверены (y/n)? ")
        result = input().lower()
        if result != "n" and result != "y":
            print("Ожидалось получить ответ либо \"y\" либо \"n\".")
    if result == "y":
        return True
    else:
        return False

def get_memory_usage(function):
    start()
    function()
    result = get_traced_memory()
    stop()
    return result[1]

def get_percent_template():
    return "\rЗавершено на {:.2f}%"

def calc_percent(value, total, arrlen, step):
    return value*100/(4*total*(arrlen/step))

def print_percent(value, total, arrlen, step):
    print(get_percent_template().format(calc_percent(value, total, arrlen, step)))

def mem_repeat(function, times, do_print=False):
    mem = 0
    
    for i in range(times):
        if do_print:
            print(i)
        start()
        result = function()
        mem += get_traced_memory()[1]
        result.pop(0)
        stop()
    return mem / times

def repeat(function, times, do_print=False):
    time_total = 0
    result = None
    start = time()

    for i in range(times):
        if do_print:
            print(i)
        result = function()

    time_total = time() - start
    
    return time_total / times
