from time import time

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

def get_percent_template():
    return "\rЗавершено на {:.2f}%"

def calc_percent(value, total, arrlen, step):
    return value*100/(2*total*(arrlen/step))

def print_percent(value, total, arrlen, step):
    print(get_percent_template().format(calc_percent(value, total, arrlen, step)))

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
