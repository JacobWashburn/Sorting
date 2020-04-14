# STRETCH: implement Linear Search				
def linear_search(arr, target):
    # TO-DO: add missing code
    iterations = 0
    for v in arr:
        iterations += 1
        if v == target:
            print(f'Linear search found {target} in {iterations} iterations.')
            return True
    print(f'Linear search discovered that {target} is not in the list in {iterations} iterations.')
    return False  # not found


# STRETCH: write an iterative implementation of Binary Search 
def binary_search(arr, target):
    if len(arr) == 0:
        return 'Empty list'  # array empty
    elif target > arr[-1]:
        print('Target not in list')
        return False
    low = 0
    high = arr[-1]
    mid = len(arr) // 2
    iterations = 0
    # TO-DO: add missing code
    while mid != target:
        arr_mid = arr[mid]
        iterations += 1
        if arr[mid] == target:
            print(f'Binary search found {target} in {iterations} iterations.')
            return True
        elif arr[mid] < target:
            low = arr[mid]
            mid = mid + (len(arr[mid:high]) // 2)
        else:
            high = arr[mid]
            mid = mid - (len(arr[low:mid]) // 2)
    print(f'Binary search found {target} in {iterations} iterations.')
    return True


# STRETCH: write a recursive implementation of Binary Search
def binary_search_recursive(arr, target, low, high):
    middle = (low + high) // 2

    if len(arr) == 0:
        return -1  # array empty
    # TO-DO: add missing if/else statements, recursive calls


test_arr = range(1, 5001)
print('Length of test_arr:', len(test_arr))
print(linear_search(test_arr, 4000))
print(binary_search(test_arr, 4000))
