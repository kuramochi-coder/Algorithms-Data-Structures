
class Solution(object):
    def checkPossibilitySimple(self, nums):
        # O(n) time and O(1) space
        total_negative_slopes = 0
        for i in range(1, len(nums)):
            if nums[i - 1] > nums[i]:
                total_negative_slopes += 1
        return total_negative_slopes <= 1

    def checkPossibility(self, nums):
        invalid_index = -1
        for i in range(len(nums) - 1):
            if nums[i] > nums[i+1]:
                if invalid_index != -1:
                    return False
                invalid_index = i

        if invalid_index == -1:
            return True
        if invalid_index == 0:
            return True
        if invalid_index == len(nums) - 2:
            return True
        if nums[invalid_index] <= nums[invalid_index + 2]:
            return True
        if nums[invalid_index - 1] <= nums[invalid_index + 1]:
            return True
        return False

print(Solution().checkPossibilitySimple([4, 1, 2]))
# True

print(Solution().checkPossibilitySimple([3, 2, 4, 1]))
# False

print(Solution().checkPossibility([4, 1, 2]))
# True

print(Solution().checkPossibility([3, 2, 4, 1]))
# False