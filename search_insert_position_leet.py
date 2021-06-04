# Search Insert Position
# Given a sorted array of distinct integers and a target value, return the index if the target is found. 
# If not, return the index where it would be if it were inserted in order.
# You must write an algorithm with O(log n) runtime complexity.

class Solution:
    def searchInsert(self, nums, target):    
        for index, num in enumerate(nums):
            if num == target:
                return index
            
        nums.append(target)
        nums = sorted(nums)
        
        for index, num in enumerate(nums):
            if num == target:
                return index

print(Solution().searchInsert([1,3,5,6], 5))
# 2
print(Solution().searchInsert([1,3,5,6], 2))
# 1
print(Solution().searchInsert([1,3,5,6], 7))
# 4
print(Solution().searchInsert([1,3,5,6], 0))
# 0