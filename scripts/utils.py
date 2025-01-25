from time import time
from sorting_algorithms import *

ARRAY_LENGTH = 1000
# ARRAY_LENGTH = 500
# ARRAY_LENGTH = 100
SORT_REPEATS = 100

SORTING_FUNCTIONS = (
    bubble_sort,
    selection_sort,
    merge_sort,
    quick_sort,
    quick_sort_median_pivot,
    builtin_power_sort,
    lsd_radix_sort
)

STEP = 10

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
