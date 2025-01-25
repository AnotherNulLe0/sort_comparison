from .sorting_algorithms import *

# Тесты сортировок
ARRAY_LENGTH = 1000
SORT_REPEATS = 100
STEP = 10

SORTING_FUNCTIONS = (
    bubble_sort,
    selection_sort,
    merge_sort,
    quick_sort,
    quick_sort_median_pivot,
    builtin_power_sort,
    lsd_radix_sort
)

# Настройки отрисовки
DOT_SIZE = 6
COLORS = (
    (1, 0, 0), 
    (0, 1, 0), 
    (0, 0, 1), 
    (1, 0.88, 0), 
    (0.65, 0.2, 0.75), 
    (0, 1, 1), 
    (0, 0, 0)
)