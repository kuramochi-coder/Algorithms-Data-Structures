# Jump Game II
# Given an array of non-negative integers nums, you are initially positioned at the first index of the array.
# Each element in the array represents your maximum jump length at that position.
# Your goal is to reach the last index in the minimum number of jumps.
# You can assume that you can always reach the last index.

# Input: nums = [2,3,1,1,4]
# Output: 2
# Explanation: The minimum number of jumps to reach the last index is 2. Jump 1 step from index 0 to 1, then 3 steps to the last index.

# Input: nums = [2,3,0,1,4]
# Output: 2

def jumpToEnd(nums):
    hops = [float('inf')] * len(nums)
    hops[0] = 0

    for i, n in enumerate(nums):
        for j in range(1, n + 1):
            if i + j < len(hops):
                hops[i + j] = min(hops[i + j], hops[i] + 1)
            else:
                break
    return hops[-1]


print(jumpToEnd([3, 2, 5, 1, 1, 9, 3, 4]))
# 2