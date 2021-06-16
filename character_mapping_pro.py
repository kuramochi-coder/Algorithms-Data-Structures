# Isomorphic Strings
# Given two strings s and t, determine if they are isomorphic.
# Two strings s and t are isomorphic if the characters in s can be replaced to get t.
# All occurrences of a character must be replaced with another character while preserving the order of characters. 
# No two characters may map to the same character, but a character may map to itself.

class Solution:
    def has_character_map(self, s1, s2):
        if len(s1) != len(s2):
            return False

        chars = {}
        for i in range(len(s1)):
            if s1[i] not in chars:
                chars[s1[i]] = s2[i]
            else:
                if chars[s1[i]] != s2[i]:
                    return False
        return True

class Solution2:
    def isIsomorphic(self, s, t):
        if s is None or t is None or len(s) != len(t):
            return False
        
        s_map, t_map = {}, {}
        
        for i in range(len(s)):
            if s[i] not in s_map:
                s_map[s[i]] = t[i]
            else:
                if s_map[s[i]] != t[i]:
                    return False
            
            if t[i] not in t_map:
                t_map[t[i]] = s[i]
            else:
                if t_map[t[i]] != s[i]:
                    return False
        return True

print(Solution().has_character_map('abc', 'def'))
# True

print(Solution().has_character_map('aac', 'def'))
# False

print(Solution2().isIsomorphic('abc', 'def'))
# True

print(Solution2().isIsomorphic('aac', 'def'))
# False