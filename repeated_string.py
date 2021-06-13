
class Solution:
    def repeatedString(self, s, n):
        count = 0
        
        for string in s:
            if string == 'a':
                count += 1
        
        count *= n // len(s)
        
        for rem_str in s[:n%len(s)]:
            if rem_str == 'a':
                count += 1
        
        return count

print(Solution().repeatedString('aba', 10))
# Expected Output: 7

print(Solution().repeatedString('abcac', 10))
# Expected Output: 4