import heapq
import random

class Solution(object):
    def findKthLargestSlow(self, nums, k):
        nums.sort()
        for i in range(k):
            if i == k - 1:
                result = nums.pop()
            else:
                nums.pop()
        return result

    def findKthLargest(self, nums, k):
        nums.sort()
        return nums[len(nums) - k]

    def findKthLargest2(self, nums, k):
        return heapq.nlargest(k, nums)[-1]


    def findKthLargest3(self, nums, k):
        def select(list, l, r, index):
            if l == r:
                return list[l]
            pivot_index = random.randint(l, r)
            # move pivot to the beginning of list
            list[l], list[pivot_index] = list[pivot_index], list[l]
            # partition
            i = l
            for j in range(l + 1, r + 1):
                if list[j] < list[l]:
                    i += 1
                    list[i], list[j] = list[j], list[i]
            # move pivot to the correct location
            list[i], list[l] = list[l], list[i]
            # recursively partition one side
            if index == i:
                return list[i]
            elif index < i:
                return select(list, l, i - 1, index)
            else:
                return select(list, i + 1, r, index)
        return select(nums, 0, len(nums) - 1, len(nums) - k)


print(Solution().findKthLargestSlow([3, 5, 2, 4, 6, 8], 3))
print(Solution().findKthLargest([3, 5, 2, 4, 6, 8], 3))
print(Solution().findKthLargest2([3, 5, 2, 4, 6, 8], 3))
print(Solution().findKthLargest3([3, 5, 2, 4, 6, 8], 3))
# 5