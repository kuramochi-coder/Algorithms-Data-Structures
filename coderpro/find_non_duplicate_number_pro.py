
class Solution(object):

    def singleNumber(self, nums):
        occurrence = {}

        for n in nums:
            occurrence[n] = occurrence.get(n, 0) + 1

        for key, value in occurrence.items():
            if value == 1:
                return key

    def singleNumber2(self, nums):
        unique = 0
        for n in nums:
            unique ^= n #this is the XOR operator which returns True only when both elements are different: e.g. 1 XOR 0 is True
            # print(unique)
        return unique

print(Solution().singleNumber([4, 3, 2, 4, 1, 3, 2]))
print(Solution().singleNumber2([4, 3, 2, 4, 1, 3, 2]))
# 1