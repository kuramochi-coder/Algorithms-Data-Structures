# String to Integer (atoi)
# Implement the myAtoi(string s) function, which converts a string to a 32-bit signed integer (similar to C/C++'s atoi function).

# The algorithm for myAtoi(string s) is as follows:

# Read in and ignore any leading whitespace.
# Check if the next character (if not already at the end of the string) is '-' or '+'. Read this character in if it is either. This determines if the final result is negative or positive respectively. Assume the result is positive if neither is present.
# Read in next the characters until the next non-digit charcter or the end of the input is reached. The rest of the string is ignored.
# Convert these digits into an integer (i.e. "123" -> 123, "0032" -> 32). If no digits were read, then the integer is 0. Change the sign as necessary (from step 2).
# If the integer is out of the 32-bit signed integer range [-231, 231 - 1], then clamp the integer so that it remains in the range. Specifically, integers less than -231 should be clamped to -231, and integers greater than 231 - 1 should be clamped to 231 - 1.
# Return the integer as the final result.


class Solution:
    def myAtoi(self, s):
        s = s.strip()
        
        if not s:
            return 0
        
        negative = False
        result = 0
        
        if s[0] == "-":
            negative = True
        elif s[0] == "+":
            negative = False
        elif not s[0].isnumeric():
            return 0
        else:
            result = ord(s[0]) - ord("0")
            
        for i in range(1, len(s)):
            
            if s[i].isnumeric():
                
                result = result * 10 + (ord(s[i]) - ord("0"))
                
            else:
                break
                
        if negative:
            result *= -1
            
        if result >= 2**31 -1:
            return 2**31 -1
        elif result < -2**31:
            return -2**31
        
        return result

print(Solution().myAtoi("4193 with words"))
# 4193
print('---')
print(Solution().myAtoi("   -42"))
# -42