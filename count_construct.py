""" 
m = target length, n = wordbank length
without memoization: time complexity is O(n^m * n) and space complexity is O(m^2)
with memoization: time complexity is O(n*m^2) and space complexity is O(m^2)
"""
def count_construct(target, wordbank, memo=None):
    if memo is None:
        memo = {}

    if target in memo:
        return memo[target]

    if target == "":
        return 1

    total_count = 0

    for word in wordbank:
        # find prefix happens when index of word is zero
        if target.find(word) == 0:
            suffix = target[len(word):]
            current_count = count_construct(suffix, wordbank, memo)
            total_count += current_count
    
    memo[target] = total_count
    return total_count

""" 
m = target length, n = wordbank length
with tabulation: time complexity is O(n*m^2) and space complexity is O(m)
"""
def count_construct_tabulation(target, wordbank):
    table = [0 for _ in range(len(target)+1)]
    table[0] = 1
    
    for i in range(len(target)+1):
        if table[i] != 0:
            for word in wordbank:
                # check if word matches the characters at position i
                if target[i:len(word)+i] == word:
                    if i + len(word) <= len(target):
                        table[i+len(word)] += table[i]
    
    return table[len(target)]

if __name__ == '__main__':
    print(count_construct("purple", ["purp", "p", "ur", "le", "purpl"])) #2
    print(count_construct("abcdef", ["ab", "abc", "cd", "def", "abcd"])) #1
    print(count_construct("skateboard", ["bo", "rd", "ate", "t", "ska", "sk", "boar"])) #0
    print(count_construct("enterapotentpot", ["a", "p", "ent", "enter", "ot", "o", "t"])) #4
    print(count_construct("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef", ["e", "eee", "eeee", "eeeee", "eeeeee", "eeeeeeee", "eeeeeee"])) #0
    print('###############################')
    print(count_construct_tabulation("purple", ["purp", "p", "ur", "le", "purpl"])) #2
    print(count_construct_tabulation("abcdef", ["ab", "abc", "cd", "def", "abcd"])) #1
    print(count_construct_tabulation("skateboard", ["bo", "rd", "ate", "t", "ska", "sk", "boar"])) #0
    print(count_construct_tabulation("enterapotentpot", ["a", "p", "ent", "enter", "ot", "o", "t"])) #4
    print(count_construct_tabulation("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef", ["e", "eee", "eeee", "eeeee", "eeeeee", "eeeeeeee", "eeeeeee"])) #0