from collections import defaultdict

class Solution:
    def canConstruct(self, ransomNote, magazine):
        hash_map = {}
        
        for letter in magazine:
            if letter not in hash_map:
                hash_map[letter] = 1
            else:
                hash_map[letter] += 1
        
        for char in ransomNote:
            if char in hash_map:
                if hash_map[char] <= 0:
                    return False

                hash_map[char] -= 1
            else:
                return False
                
        return True

#  solution below by coder pro
    def canSpell(self, magazine, note):
        letters = defaultdict(int)
        for c in magazine:
            letters[c] += 1

        for c in note:
            if letters[c] <= 0:
                return False
            letters[c] -= 1

        return True

print(Solution().canSpell(['a', 'b', 'c', 'd', 'e', 'f'], 'bed'))
# True

print(Solution().canSpell(['a', 'b', 'c', 'd', 'e', 'f'], 'cat'))
# False

print(Solution().canConstruct('bed', ['a', 'b', 'c', 'd', 'e', 'f']))
# True

print(Solution().canConstruct('cat', ['a', 'b', 'c', 'd', 'e', 'f']))
# False