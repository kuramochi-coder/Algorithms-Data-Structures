# Range Sum Query - Immutable
# Given an integer array nums, handle multiple queries of the following type:
# Calculate the sum of the elements of nums between indices left and right inclusive where left <= right.
# Implement the NumArray class:
# NumArray(int[] nums) Initializes the object with the integer array nums.
# int sumRange(int left, int right) Returns the sum of the elements of nums between indices left and right inclusive (i.e. nums[left] + nums[left + 1] + ... + nums[right]).

class ListFastSum(object):
    def __init__(self, nums):
        # self.pre = [0]
        self.pre = []

        sum = 0
        for num in nums:
            sum += num
            self.pre.append(sum)

    def sum(self, start, end):
        if start == 0:
            return self.pre[end]
        else:
            return self.pre[end] - self.pre[start-1]



print(ListFastSum([1, 2, 3, 4, 5, 6, 7]).sum(2, 4))
# 12
print(ListFastSum([1, 2, 3, 4, 5, 6, 7]).sum(2, 5))
# 18