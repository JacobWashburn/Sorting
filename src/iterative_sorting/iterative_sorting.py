import random


# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    total = 0
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):

        cur_index = i
        # TO-DO: find next
        # (hint, can do in 3 loc)
        smallest_element = [cur_index, arr[i]]
        for v in range(cur_index, len(arr)):
            total += 1
            stuff = ['index', v, 'value', arr[v]]
            smallest_element = [v, arr[v]] if smallest_element[1] > arr[v] else smallest_element
        # TO-DO: swap
        arr[smallest_element[0]] = arr[cur_index]
        arr[cur_index] = smallest_element[1]
    print('selection total: ', total)
    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    count = 1
    total = 0
    while count > 0:
        count = 0
        for i in range(0, len(arr)):
            total += 1
            cur_index = arr[i]
            next_index = arr[i + 1] if cur_index != arr[-1] else arr[i]
            if cur_index > next_index:
                arr[i] = next_index
                arr[i + 1] = cur_index
                count += 1
    print('bubble total: ', total)
    return arr


# STRETCH: implement the Count Sort function below
def count_sort(arr, maximum = -1):
    for v in arr:
        if v > maximum:
            maximum = v
    index_list = [0] * (maximum + 1)
    for v in arr:
        if v >= 0:
            index_list[v] += 1
        else:
            return "Error, negative numbers not allowed in Count Sort"
    arr.clear()
    for v in range(len(index_list)):
        while index_list[v] > 0:
            arr.append(v)
            index_list[v] -= 1
    return arr


test_arr = [1, 5, 8, 4, 2, 9, 6, 0, 3, 7]
test_arr2 = [1, 5, 8, 4, 2, 9, 6, 0, 3, 7]
test_arr3 = [1, 5, 8, 4, 2, 9, 6, 0, 3, 7]
test_arr4 = [1, 0, 5, 4, 2, 9, 6, 0, 3, 7, 2, 9, 6, 0, 3, 7]
# test_arr5 = random.sample(range(2000000), 500000)
print(selection_sort(test_arr))
print(bubble_sort(test_arr2))
print(count_sort(test_arr3))
print(count_sort(test_arr4))
# print(count_sort(test_arr5))
