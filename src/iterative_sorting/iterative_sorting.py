# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):

    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        # TO-DO: find next
        # (hint, can do in 3 loc)
        smallest_element = [cur_index, arr[i]]
        for v in range(cur_index, len(arr)):
            stuff = ['index', v, 'value', arr[v]]
            smallest_element = [v, arr[v]] if smallest_element[1] > arr[v] else smallest_element
        # TO-DO: swap
        arr[smallest_element[0]] = arr[cur_index]
        arr[cur_index] = smallest_element[1]
    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):

    return arr


# STRETCH: implement the Count Sort function below
def count_sort(arr, maximum = -1):
    return arr


test_arr = [1, 5, 8, 4, 2, 9, 6, 0, 3, 7]
print(selection_sort(test_arr))
