
class Solution:
    def jumpingOnClouds(self, c):
        start = 0
        total_jumps = 0
        
        while start < len(c) - 1:
            if start + 2 < len(c) and c[start + 2] == 0:
                start += 2
                total_jumps += 1
            elif start + 1 < len(c) and c[start + 1] == 0:
                start += 1
                total_jumps += 1
        
        
        return total_jumps

print(Solution().jumpingOnClouds([0, 0, 0, 0, 1, 0]))
# Output 3