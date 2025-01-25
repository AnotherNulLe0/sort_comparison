def bubble_sort(array):
    new_array = array.copy()
    n = len(new_array)
    for i in range(0, n-1):
        for j in range(0, n-1-i):
            if new_array[j] > new_array[j+1]:
                new_array[j], new_array[j+1] = new_array[j+1], new_array[j]
    return new_array

def selection_sort(array):
    new_array = array.copy()
    n = len(new_array)
    for i in range(0, n-1):
        for j in range(i+1, n):
            if new_array[i] > new_array[j]:
                new_array[i], new_array[j] = new_array[j], new_array[i]
    return new_array

def merge_sort(input_array):
    if len(input_array) == 1 or len(input_array) == 0:
        return input_array

    first_half = merge_sort(input_array[:len(input_array) // 2])
    second_half = merge_sort(input_array[len(input_array) // 2:])

    n = m = k = 0

    sorted_array = [0] * len(input_array)

    while n < len(first_half) and m < len(second_half):
        if first_half[n] <= second_half[m]:
            sorted_array[k] = first_half[n]
            n += 1
        else:
            sorted_array[k] = second_half[m]
            m += 1
        k += 1

    while n < len(first_half):
        sorted_array[k] = first_half[n]
        n += 1
        k += 1

    while m < len(second_half):
        sorted_array[k] = second_half[m]
        m += 1
        k += 1

    return sorted_array

def quick_sort_median_pivot(array):
    return quick_sort(array, len(array)//2)

def quick_sort(array, pivot_point=0):
    less = []
    equal = []
    greater = []

    if len(array) > 1:
        pivot = array[pivot_point]
        for x in array:
            if x < pivot:
                less.append(x)
            elif x == pivot:
                equal.append(x)
            elif x > pivot:
                greater.append(x)
        return quick_sort(less) + equal + quick_sort(greater)
    else:
        return array

def builtin_power_sort(array):
    return sorted(array)

def lsd_radix_sort(array):
    arr = array.copy()
    max_digits = max([len(str(x)) for x in arr])

    bins = [[] for _ in range(10)]

    for i in range(0, max_digits):
        for x in arr:
            digit = (x // 10 ** i) % 10
            bins[digit].append(x)
        arr = [x for queue in bins for x in queue]
        bins = [[] for _ in range(10)]
    return arr