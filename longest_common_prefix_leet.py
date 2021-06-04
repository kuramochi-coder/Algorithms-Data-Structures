# Longest Common Prefix
# Write a function to find the longest common prefix string amongst an array of strings.
# If there is no common prefix, return an empty string "".

class Solution:
    def longestCommonPrefix(self, strs):
        result = ''
        index = 0
        
        if strs is None or len(strs) == 0:
            return result

        # for char in first word strs[0] in list of strings, compare against the next word strs[1] onwards
        # if index exceeds length of the string we are comparing to or the characters do not match, return 
        for char in strs[0]:
            for i in range(1, len(strs)):
                if index >= len(strs[i]) or char != strs[i][index]:
                    return result
                
            # if char matches for all the words in list, we can add it to result
            result += char
            index += 1
        
        return result

    def longestCommonPrefix2(self, strs):
        result = ""
        i = 0
        
        while True:
            try:
                sets = set(string[i] for string in strs)
                if len(sets) == 1:
                    result += sets.pop()
                    i += 1
                else:
                    break
            except Exception as e:
                break
                
        return result

print(Solution().longestCommonPrefix(["flower","flow","flight"]))
# "fl"
print('---')
print(Solution().longestCommonPrefix(["dog","racecar","car"]))
# ""
print('---')
print(Solution().longestCommonPrefix2(["flower","flow","flight"]))
# "fl"
print('---')
print(Solution().longestCommonPrefix2(["dog","racecar","car"]))
# ""

