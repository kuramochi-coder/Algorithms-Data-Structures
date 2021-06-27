# Longest Increasing Subsequence
# Given an integer array nums, return the length of the longest strictly increasing subsequence.
# A subsequence is a sequence that can be derived from an array by deleting some or no elements without changing the order of the remaining elements. 
# For example, [3,6,2,7] is a subsequence of the array [0,3,1,6,2,2,7].
# Input: nums = [10,9,2,5,3,7,101,18]
# Output: 4
# Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.

def longest_increasing_subsequence(arr):
    cache = [1] * len(arr)
    for i in range(1, len(arr)):
        for j in range(i):
            if arr[i] > arr[j]:
                cache[i] = max(cache[i], cache[j] + 1)
    return max(cache)


print(longest_increasing_subsequence(
    [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3]))
# 5