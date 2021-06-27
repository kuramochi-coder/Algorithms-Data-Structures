nums = [2, 7, 8, 9, 10, 13, 17, 19, 21]

""" 
n: length of array
time complexity is O(logn) and space complexity is O(1)
"""
def binary_search_iterative(array, target):
    left = 0
    right = len(array) - 1

    while left <= right:
        mid = (left + right) // 2

        if target == array[mid]:
            return mid
        elif target < array[mid]:
            right = mid - 1
        elif target > array[mid]:
            left = mid + 1

    return False


""" 
n: length of array
time complexity is O(logn) and space complexity is O(logn)
"""
def binary_search_recursive(array, target):
    return binary_search_recursive_helper(array, target, 0, len(array) - 1)

def binary_search_recursive_helper(array, target, left, right):
    if left >= right:
        return False

    mid = (left + right) // 2

    if target == array[mid]:
        return mid
    elif target < array[mid]:
        # right = mid - 1
        return binary_search_recursive_helper(array, target, left, mid - 1)
    elif target > array[mid]:
        # left = mid + 1
        return binary_search_recursive_helper(array, target, mid + 1, right)

print(binary_search_iterative(nums, 7))
print(binary_search_iterative(nums, 15))
print('###############################')
print(binary_search_recursive(nums, 7))
print(binary_search_recursive(nums, 15))