
class Solution:
    def rotLeft(self, a, d):
        result = [0] * len(a)
        
        for i in range(len(a)):
            result[i-d] = a[i]
        
        return result

print(Solution().rotLeft([1, 2, 3, 4, 5], 4))
# [5, 1, 2, 3, 4]