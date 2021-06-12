# Minimum Size Subarray Sum
# Given an array of positive integers nums and a positive integer target, 
# return the minimal length of a contiguous subarray [numsl, numsl+1, ..., numsr-1, numsr] of which the sum is greater than or equal to target. 
# If there is no such subarray, return 0 instead.

# Input: target = 7, nums = [2,3,1,2,4,3]
# Output: 2
# Explanation: The subarray [4,3] has the minimal length under the problem constraint.

class Solution(object):
    def minSubArray(self, k, nums):
        leftIndex = rightIndex = 0
        sum = 0
        minLen = float('inf')

        while rightIndex < len(nums):
            sum += nums[rightIndex]
            while sum >= k:
                minLen = min(minLen, rightIndex - leftIndex + 1)
                sum -= nums[leftIndex]
                leftIndex += 1
            rightIndex += 1
        
        if minLen == float('inf'):
            return 0
        return minLen

print(Solution().minSubArray(7, [2, 3, 1, 2, 4, 3]))
# 2