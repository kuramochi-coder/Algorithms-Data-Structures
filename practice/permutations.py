""" 
n: length of array
time complexity is O(n!) and space complexity is O(n^2)
"""
class Solution:
    def permutations(self, elements):
        if len(elements) == 0:
            return [[]]

        first_element = elements[0]
        rest_of_elements = elements[1:]

        permutations_without_first = self.permutations(rest_of_elements)

        final_permutations = []

        for perm in permutations_without_first:
            for i in range(len(perm)+1):
                perm_with_first = [*perm[:i], first_element, *perm[i:]] #similar to spread operator in javascript 
                final_permutations.append(perm_with_first)
        
        return final_permutations

# solution below by coder pro
    def permute(self, nums):
        return self._permuteHelper(nums)

    def _permuteHelper(self, nums, start=0):
        if start == len(nums) - 1:
            return [nums[:]]

        result = []
        for i in range(start, len(nums)):
            nums[start], nums[i] = nums[i], nums[start]
            result += self._permuteHelper(nums, start + 1)
            nums[start], nums[i] = nums[i], nums[start]
        return result

    def permute2(self, nums, values=[]):
        if not nums:
            return [values]
        result = []
        for i in range(len(nums)):
            result += self.permute2(nums[:i] + nums[i+1:], values + [nums[i]])
        return result

    def permute2Iterative(self, nums):
        results = []
        stack = [(nums, [])]
        while len(stack):
            nums, values = stack.pop()
            if not nums:
                results += [values]
            for i in range(len(nums)):
                stack.append((nums[:i]+nums[i+1:], values+[nums[i]]))
        return results

  

print(Solution().permutations(['a', 'b', 'c']))
print(Solution().permutations(['b', 'c']))
print('--')
print(Solution().permute([1, 2, 3]))
# [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 2, 1], [3, 1, 2]]

print(Solution().permute2([1, 2, 3]))
# [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 2, 1], [3, 1, 2]]

print(Solution().permute2Iterative([1, 2, 3]))
# [[3, 2, 1], [3, 1, 2], [2, 3, 1], [2, 1, 3], [1, 3, 2], [1, 2, 3]]