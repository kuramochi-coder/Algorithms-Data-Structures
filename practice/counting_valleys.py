
class Solution:
    def countingValleys(self, path):
    # Write your code here
        current_level = 0
        valley_count = 0
        
        for p in path:
            if p == 'D':
                initial_level = current_level
                current_level -= 1
                if initial_level >= 0 and current_level < 0:
                    valley_count += 1
            else:
                current_level += 1
                
        return valley_count

print(Solution().countingValleys('UDDDUDUU'))
# output: 1
print(Solution().countingValleys('DDUUDDUDUUUD'))
# output: 2