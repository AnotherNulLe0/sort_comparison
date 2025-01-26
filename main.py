from scripts.utils import promt
from scripts.cfg import ARRAY_LENGTH, SORT_REPEATS, STEP, SORTING_FUNCTIONS
from scripts.graph_draw import draw
from scripts.efficiency_test import run
from sys import argv
from os import remove, listdir
from os.path import isfile
from json import load, dump
from time import localtime

def test(arr_length=ARRAY_LENGTH, repeats=SORT_REPEATS, step=STEP):
    print("Тестируются алгоритмы сортировки. Это может занять несколько минут.")
    print("Параметры:")
    print(f"\tДлинна массива для сортировки: {arr_length}")
    print(f"\tПовторных вызовов функции: {repeats}")
    print(f"\tИзменение длины массива: {step}")
    return run(arr_length, repeats, step, SORTING_FUNCTIONS)
        

def write_efficiency(sorted_efficiency, unsorted_efficiency, sorted_memory, unsorted_memory):
    cur_time = localtime()
    cur_time = f"{cur_time.tm_year}-{cur_time.tm_mon}-{cur_time.tm_mday} {cur_time.tm_sec}{cur_time.tm_min}{cur_time.tm_hour}"
    buf = {"sorted_time": sorted_efficiency, 
           "unsorted_time": unsorted_efficiency,
           "sorted_memory": sorted_memory,
           "unsorted_memory": unsorted_memory
          }
    with open(f"./results/{cur_time}.json", "w") as f:
        dump(buf, f)

def read_data(specified_data=None):
    sorted_efficiency = None
    unsorted_efficiency = None
    sorted_memory = None
    unsorted_memory = None

    try:
        path = specified_data
        if not path:
            files = filter(lambda x: isfile("./results/"+x), listdir("./results/"))
            latest = max(files)
            path = latest
        with open(f"./results/{path}", "r") as f:
            result = load(f)
            unsorted_efficiency, sorted_efficiency = result["unsorted_time"], result["sorted_time"]
            unsorted_memory, sorted_memory = result["unsorted_memory"], result["sorted_memory"]
    except (IOError, ValueError):
        print("Данные тестов не были найдены.")
        if specified_data:
            return
        sorted_efficiency, unsorted_efficiency, sorted_memory, unsorted_memory  = test()
        write_efficiency(sorted_efficiency, unsorted_efficiency, sorted_memory, unsorted_memory)
    draw(sorted_efficiency, unsorted_efficiency, sorted_memory, unsorted_memory)

def remove_test(path=None, is_all=False):
    dir = listdir("./results/")
    dir.remove("placeholder")
    if not is_all and not path:
        files = filter(lambda x: isfile("./results/"+x), )
        if dir:
            latest = max(files)
            if promt(f"Удалить файл \"{latest}.json\"?"):
                remove(f"./results/{latest}.json")
                print("Тест удалён.")
        else:
            print("Тесты не найдены.")
    elif is_all:
            files = []
            if (files := dir):
                if promt(f"Удалить все тесты?\n  {"\n  ".join(files)}"):
                    for file in files:
                        remove("./results/"+file)
                    print("Тесты удалены.")
            else:
                print("Тесты не найдены.")
    elif path:
        if promt(f"Удалить файл \"{path}.json\"?"):
            try:
                remove(f"./results/{path}.json")
                print("Тест удалён.")
            except FileNotFoundError:
                print("Тест не найден.")

if __name__ == "__main__":
    sorted_efficiency = None
    unsorted_efficiency = None
    match len(argv):
        case 1:
            read_data()
        case 2:
            match argv[1]:
                case "--generate" | "-g":
                    s, u, ms, mu = test()
                    write_efficiency(s, u, ms, mu)
                    draw(s, u, ms, mu)
                case "--read" | "-r":
                    read_data()
                case "--clear" | "-c":
                    remove_test()
                case _:
                    print("Неизвестный флаг.")
        case 3:
            match argv[1]:
                case "--generate" | "-g":
                    s, u, ms, mu = test(int(argv[2]))
                    write_efficiency(s, u, ms, mu)
                    draw(s, u, ms, mu)
                case "--read" | "-r":
                    read_data(argv[2])
                case "--clear" | "-c":
                    if argv[2] == "--all":
                        remove_test(is_all=True)
                    else:
                        remove_test(argv[2])
                case _:
                    print("Неизвестный флаг.")
        case 4:
            match argv[1]:
                case "--generate" | "-g":
                    s, u, ms, mu = test(int(argv[2]), int(argv[3]))
                    write_efficiency(s, u, ms, mu)
                    draw(s, u, ms, mu)
                case _:
                    print("Неизвестный флаг.")
        case 5:
            match argv[1]:
                case "--generate" | "-g":
                    s, u, ms, mu = test(int(argv[2]), int(argv[3]), int(argv[4]))
                    write_efficiency(s, u, ms, mu)
                    draw(s, u, ms, mu)
                case _:
                    print("Неизвестный флаг.")
        case _:
            print("Программа принимает не больше 3 аргументов.")

