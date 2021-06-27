# aim is to find 3 numbers that sum to zero

class Solution:
    def threeSumBruteForce(self, nums):
        result = []
        for i1 in range(0, len(nums)):
            for i2 in range(i1+1, len(nums)):
                for i3 in range(i2+1, len(nums)):
                    a, b, c = nums[i1], nums[i2], nums[i3]
                    if a + b + c == 0:
                        result.append([a, b, c])
        return result

    def threeSumHashmap(self, nums):
        nums.sort()
        result = []
        for i in range(len(nums)):
            self.twoSumHashmap(nums, i, result)
        return result

    def twoSumHashmap(self, nums, start, result):
        values = {}
        target = -nums[start]
        for i in range(start+1, len(nums)):
            n = nums[i]
            diff = target - n
            if diff in values:
                result.append([n, diff, nums[start]])
            values[n] = 1

    def threeSumIndices(self, nums):
        nums.sort()
        result = []
        for i in range(len(nums)):
            self.twoSumIndices(nums, i, result)
        return result

    def twoSumIndices(self, nums, start, result):
        low = start + 1
        high = len(nums) - 1
        while low < high:
            sum = nums[start] + nums[low] + nums[high]
            if sum == 0:
                result.append([nums[start], nums[low], nums[high]])
                low += 1
                high -= 1
            elif sum < 0:
                low += 1
            else:
                high -= 1


print(Solution().threeSumBruteForce([-1, 0, 1, 2, -4, -3]))
# [[-1, 0, 1], [1, 2, -3]]

print(Solution().threeSumHashmap([-1, 0, 1, 2, -4, -3]))
# [[2, 1, -3], [1, 0, -1]]

print(Solution().threeSumIndices([-1, 0, 1, 2, -4, -3]))
# [[-3, 1, 2], [-1, 0, 1]]