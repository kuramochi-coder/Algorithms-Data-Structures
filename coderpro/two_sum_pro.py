
class Solution:
    def twoSumBruteForce(self, nums, target):
        for (i1, num1) in enumerate(nums):
            for (i2, num2) in enumerate(nums):
                if num1 == num2:
                    continue
                if num1 + num2 == target:
                    return [i1, i2]
        
        return []

    def twoSum(self, nums, target):
        values = {}

        for (index, num) in enumerate(nums):
            difference =  target - num

            if difference in values:
                return [index, values[difference]]
            
            values[num] = index
        
        return []

# solutions below by coder pro
    def twoSumA(self, nums, target):
        for i1, a in enumerate(nums):
            for i2, b in enumerate(nums):
                if a == b:
                    continue
                if a + b == target:
                    return [i1, i2]
        return []

    def twoSumB(self, nums, target):
        values = {}
        for i, num in enumerate(nums):
            diff = target - num
            if diff in values:
                return [i, values[diff]]
            values[num] = i
        return []

print(Solution().twoSumBruteForce([2, 7, 11, 15], 18))
print(Solution().twoSum([2, 7, 11, 15], 18))
print(Solution().twoSumA([2, 7, 11, 15], 18))
print(Solution().twoSumB([2, 7, 11, 15], 18))