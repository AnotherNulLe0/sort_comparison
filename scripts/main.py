from utils import *
from graph_draw import *
from efficiency_test import *
from sys import argv
from os import remove
from json import load, dump

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
    with open("results/data1.json", "w") as f:
        dump(sorted_efficiency, f)
    with open("results/data2.json", "w") as f:
        dump(unsorted_efficiency, f)

def read_data():
    sorted_efficiency = None
    unsorted_efficiency = None

    try:
        with open("results/data1.json", "r") as f:
            sorted_efficiency = load(f)
        with open("results/data2.json", "r") as f:
            unsorted_efficiency = load(f)
    except IOError:
        if sorted_efficiency:
            print("Данные несортированного массива не были найдены.")
            unsorted_efficiency = test(is_sorted=False)
        else:
            try:
                with open("results/data2.json", "r") as f:
                    unsorted_efficiency = load(f)
                print("Данные отсортированного массива не были найдены.")
                sorted_efficiency = test(is_sorted=True)
            except IOError:
                print("Данные тестов не были найдены.")
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

    elif len(argv) == 2 and (argv[1] == "--clear" or argv[1] == "-c"):
        removed_first = False
        try:
            remove("results/data1.json")
            removed_first = True
            remove("results/data2.json")
            print("Тесты удалены.")
        except FileNotFoundError:
            try:
                remove("results/data2.json")
                print("Тесты удалены.")
            except FileNotFoundError:
                if removed_first:
                    print("Тесты удалены.")
                else:
                    print("Тесты не найдены.")

    elif len(argv) == 1:
        read_data()
    else:
        print("Неизвестный флаг.")