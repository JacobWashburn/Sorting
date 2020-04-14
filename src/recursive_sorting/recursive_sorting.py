# TO-DO: complete the helpe function below to merge 2 sorted arrays
def merge(arr_a, arr_b):
    # elements = len(arr_a) + len(arr_b)
    print('\n---- start of merge ----')
    merged_arr = []
    # TO-DO
    while len(arr_a) > 0 and len(arr_b) > 0:
        if arr_a[0] < arr_b[0]:
            print('merged_arr:', merged_arr, '-- low:', arr_a, '-- high', arr_b)
            merged_arr.append(arr_a[0])
            arr_a.pop(0)
        else:
            print('merged_arr:', merged_arr, '-- low:', arr_a, '-- high: ', arr_b)
            merged_arr.append(arr_b[0])
            arr_b.pop(0)
    remainder = arr_b if not len(arr_a) else arr_a
    while len(remainder):
        print('merged_arr:', merged_arr, '-- remainder:', remainder)
        merged_arr.append(remainder[0])
        remainder.pop(0)
    print('\n')
    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort(arr):
    # TO-DO
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    print('mid:', mid, '-- low:', arr[:mid], '-- high:', arr[mid:])

    recursive_low = merge_sort(arr[:mid])
    recursive_high = merge_sort(arr[mid:])

    return merge(recursive_low, recursive_high)


test_arr = [1, 5, 8, 4, 2, 9, 6, 0, 7, 3, 4]
print('Starting point:', test_arr, '\nFinal result:  ', merge_sort(test_arr))


# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr


def merge_sort_in_place(arr, l, r):
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort(arr):
    return arr
