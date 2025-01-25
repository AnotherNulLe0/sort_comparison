from scripts.utils import *
from scripts.graph_draw import *
from scripts.efficiency_test import *
from sys import argv
from os import remove, listdir
from os.path import isfile, relpath
from json import load, dump
from time import localtime

def test(arr_length=ARRAY_LENGTH, repeats=SORT_REPEATS, step=STEP, sorted=None, unsorted=None):
    print("Тестируются алгоритмы сортировки. Это может занять несколько минут.")
    print("Параметры:")
    print(f"\tДлинна массива для сортировки: {arr_length}")
    print(f"\tПовторных вызовов функции: {repeats}")
    print(f"\tИзменение длины массива: {step}")
    if sorted and not unsorted:
        return run(arr_length, repeats, step, SORTING_FUNCTIONS, sorted_efficiency=sorted)
    elif unsorted and not sorted:
        return run(arr_length, repeats, step, SORTING_FUNCTIONS, unsorted_efficiency=unsorted)
    else:
        return run(arr_length, repeats, step, SORTING_FUNCTIONS)

def write_efficiency(sorted_efficiency, unsorted_efficiency):
    cur_time = localtime()
    cur_time = f"{cur_time.tm_year}-{cur_time.tm_mon}-{cur_time.tm_mday} {cur_time.tm_sec}{cur_time.tm_min}{cur_time.tm_hour}"
    buf = [unsorted_efficiency, sorted_efficiency]
    with open(f"./results/{cur_time}.json", "w") as f:
        dump(buf, f)

def read_data(specified_data=None):
    sorted_efficiency = None
    unsorted_efficiency = None

    try:
        path = specified_data
        if not path:
            files = filter(lambda x: isfile("./results/"+x), listdir("./results/"))
            latest = max(files)
            path = latest
        with open(f"./results/{path}", "r") as f:
            unsorted_efficiency, sorted_efficiency = load(f)
    except (IOError, ValueError):
        print("Данные тестов не были найдены.")
        if specified_data:
            return
        sorted_efficiency, unsorted_efficiency = test()
        write_efficiency(sorted_efficiency, unsorted_efficiency)
    draw(sorted_efficiency, unsorted_efficiency)

if __name__ == "__main__":
    sorted_efficiency = None
    unsorted_efficiency = None

    if len(argv) == 2 and (argv[1] == "--generate" or argv[1] == "-g"):
        s, u = test()
        write_efficiency(s, u)
        draw(s, u)
    elif len(argv) == 3 and (argv[1] == "--generate" or argv[1] == "-g"):
        s, u = test(int(argv[2]))
        write_efficiency(s, u)
        draw(s, u)
    elif len(argv) == 4 and (argv[1] == "--generate" or argv[1] == "-g"):
        s, u = test(int(argv[2]), int(argv[3]))
        write_efficiency(s, u)
        draw(s, u)
    elif len(argv) == 5 and (argv[1] == "--generate" or argv[1] == "-g"):
        s, u = test(int(argv[2]), int(argv[3]), int(argv[4]))
        write_efficiency(s, u)
        draw(s, u)

    elif len(argv) == 2 and (argv[1] == "--read" or argv[1] == "-r"):
        read_data()
    elif len(argv) == 3 and (argv[1] == "--read" or argv[1] == "-r"):
        read_data(argv[2])

    elif len(argv) == 2 and (argv[1] == "--clear" or argv[1] == "-c"):
        files = filter(lambda x: isfile("./results/"+x), listdir("./results/"))
        latest = max(files)
        if latest:
            remove("./results/"+latest)
            print("Тест удалён.")
        else:
            print("Тест не найден.")
    elif len(argv) == 3 and (argv[1] == "--clear" or argv[1] == "-c") and argv[2] == "--all":
        files = []
        if (files := listdir("./results/")):
            for file in files:
                remove("./results/"+file)
            print("Тесты удалены.")
        else:
            print("Тесты не найдены.")
    elif len(argv) == 3 and (argv[1] == "--clear" or argv[1] == "-c"):
        try:
            remove(f"./results/{argv[2]}")
            print("Тест удалён.")
        except FileNotFoundError:
            print("Тест не найден.")

    elif len(argv) == 1:
        read_data()
    else:
        print("Неверный формат флагов.")