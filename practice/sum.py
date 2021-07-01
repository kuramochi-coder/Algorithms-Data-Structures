import sys
import time

""" 
n: size if input
time complexity is O(n^2) and space complexity is O(n)
"""
arr = [1] * 600

def slow_sum(array):
    if len(array) == 0:
        return 0

    first_element = array[0]
    rest_of_elements = array[1:]

    return first_element + slow_sum(rest_of_elements)

""" 
n: size if input
time complexity is O(n) and space complexity is O(n)
"""

def fast_sum(array):
    return fast_sum_helper(array, 0)

def fast_sum_helper(array, index):
    if index == len(array):
        return 0
    
    return array[index] + fast_sum_helper(array, index + 1)


# print(slow_sum([1, 5, 7, -2]))
slow_start_time = time.time()
print(slow_sum(arr))
slow_end_time = time.time()
print(f"--- slow completed in: {(slow_end_time - slow_start_time)*1000}ms ---")
print('###############################')
# print(fast_sum([1, 5, 7, -2]))
fast_start_time = time.time()
print(fast_sum(arr))
fast_end_time = time.time()
print(f"--- fast completed in: {(fast_end_time - fast_start_time)*1000}ms ---")