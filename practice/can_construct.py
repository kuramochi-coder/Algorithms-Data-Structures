""" 
m = target length, n = wordbank length
without memoization: time complexity is O(n^m * n) and space complexity is O(m^2)
with memoization: time complexity is O(n*m^2) and space complexity is O(m^2)
"""
def can_construct(target, wordbank, memo=None):
    if memo is None:
        memo = {}

    if target in memo:
        return memo[target]

    if target == "":
        return True

    for word in wordbank:
        # find prefix happens when index of word is zero
        if target.find(word) == 0:
            suffix = target[len(word):]
            if can_construct(suffix, wordbank, memo):
                memo[target] = True
                return True

    memo[target] = False
    return False

""" 
m = target length, n = wordbank length
with tabulation: time complexity is O(n*m^2) and space complexity is O(m)
"""
def can_construct_tabulation(target, wordbank):
    table = [False for _ in range(len(target)+1)]
    table[0] = True
    
    for i in range(len(target)+1):
        if table[i] == True:
            for word in wordbank:
                # check if word matches the characters at position i
                if target[i:len(word)+i] == word:
                    if i + len(word) <= len(target):
                        table[i+len(word)] = True
    
    return table[len(target)]


if __name__ == '__main__':
    print(can_construct("abcdef", ["ab", "abc", "cd", "def", "abcd"])) #True
    print(can_construct("skateboard", ["bo", "rd", "ate", "t", "ska", "sk", "boar"])) #False
    print(can_construct("enterapotentpot", ["a", "p", "ent", "enter", "ot", "o", "t"])) #True
    print(can_construct("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef", ["e", "eee", "eeee", "eeeee", "eeeeee", "eeeeeeee", "eeeeeee"])) #False
    print('###############################')
    print(can_construct_tabulation("abcdef", ["ab", "abc", "cd", "def", "abcd"])) #True
    print(can_construct_tabulation("skateboard", ["bo", "rd", "ate", "t", "ska", "sk", "boar"])) #False
    print(can_construct_tabulation("enterapotentpot", ["a", "p", "ent", "enter", "ot", "o", "t"])) #True
    print(can_construct_tabulation("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef", ["e", "eee", "eeee", "eeeee", "eeeeee", "eeeeeeee", "eeeeeee"])) #False