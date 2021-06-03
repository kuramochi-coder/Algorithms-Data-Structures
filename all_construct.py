""" 
m = target length, n = wordbank length
with or without memoization: time complexity is O(n^m) and space complexity is O(m)
"""

def all_construct(target, wordbank, memo=None):
    if memo is None:
        memo = {}

    if target in memo:
        return memo[target]

    if target == "":
        return [[]]

    result = []

    for word in wordbank:
        # find prefix happens when index of word is zero
        if target.find(word) == 0:
            suffix = target[len(word):]
            suffix_combinations = all_construct(suffix, wordbank, memo)
            target_combinations = [[word] + combination for combination in suffix_combinations]
            result.extend(target_combinations)

    memo[target] = result
    return result

""" 
m = target length, n = wordbank length
with tabulation: time complexity is O(n^m) and space complexity is O(n^m)
"""
def all_construct_tabulation(target, wordbank):
    table = [[] for _ in range(len(target)+1)]
    table[0] = [[]]
    
    for i in range(len(target)+1):
        for word in wordbank:
            if target[i:len(word)+i] == word:
                new_combinations = [[word] + combination for combination in table[i]]
                if i + len(word) <= len(target):
                    table[i+len(word)].extend(new_combinations)

    return table[len(target)]

if __name__ == '__main__':
    print(all_construct("purple", ["purp", "p", "ur", "le", "purpl"])) #[['purp', 'le'], ['p', 'ur', 'p', 'le']]
    print(all_construct("abcdef", ["ab", "abc", "cd", "def", "abcd"])) #[['abc', 'def']]
    print(all_construct("skateboard", ["bo", "rd", "ate", "t", "ska", "sk", "boar"])) #[]
    print(all_construct("enterapotentpot", ["a", "p", "ent", "enter", "ot", "o", "t"])) #[['enter', 'a', 'p', 'ot', 'ent', 'p', 'ot'], ['enter', 'a', 'p', 'ot', 'ent', 'p', 'o', 't'], ['enter', 'a', 'p', 'o', 't', 'ent', 'p', 'ot'], ['enter', 'a', 'p', 'o', 't', 'ent', 'p', 'o', 't']]
    print(all_construct("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef", ["e", "eee", "eeee", "eeeee", "eeeeee", "eeeeeeee", "eeeeeee"])) #[]
    print('###############################')
    print(all_construct_tabulation("purple", ["purp", "p", "ur", "le", "purpl"])) #[['purp', 'le'], ['p', 'ur', 'p', 'le']]
    print(all_construct_tabulation("abcdef", ["ab", "abc", "cd", "def", "abcd"])) #[['abc', 'def']]
    print(all_construct_tabulation("skateboard", ["bo", "rd", "ate", "t", "ska", "sk", "boar"])) #[]
    print(all_construct_tabulation("enterapotentpot", ["a", "p", "ent", "enter", "ot", "o", "t"])) #[['enter', 'a', 'p', 'ot', 'ent', 'p', 'ot'], ['enter', 'a', 'p', 'ot', 'ent', 'p', 'o', 't'], ['enter', 'a', 'p', 'o', 't', 'ent', 'p', 'ot'], ['enter', 'a', 'p', 'o', 't', 'ent', 'p', 'o', 't']]
    print(all_construct_tabulation("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef", ["e", "eee", "eeee", "eeeee", "eeeeee", "eeeeeeee", "eeeeeee"])) #[]