from tracemalloc import start, stop, get_traced_memory
from scripts.sorting_algorithms import merge_sort
from random import randint
start()

times = 5
mem = 0

# function = lambda: merge_sort([randint(1, 1000) for i in range(100)])
function = lambda: merge_sort([i for i in range(100)])

print(get_traced_memory())
stop()

for i in range(times):
    start()
    result = function()
    mem += get_traced_memory()[1]
    print(get_traced_memory())
    stop()
print(mem/times)