# Group Anagrams
# Given an array of strings strs, group the anagrams together. You can return the answer in any order.
# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, 
# typically using all the original letters exactly once.

import collections

def hashkey(str):
    return "".join(sorted(str)) # sorted returns list of characters: ['a', 'b', 'c'], join to make it 'abc'

def hashkey2(str):
    arr = [0] * 26 # 26 characters of alphabet, initialize to 0, each represents a character
    for c in str:
        arr[ord(c) - ord('a')] += 1 
    # arr looks like [1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] for 'abc'
    return tuple(arr)

# time complexity: O(n * mlogm) where m is the average length of each word and n is number of words. space complexity: O(n)
# because sorting is used for the hashing
def groupAnagramWords(strs):
    groups = {}
    for s in strs:
        key = hashkey(s)
        if key not in groups:
            groups[key] = [s]
        else:
            groups[key].append(s)
    return tuple(groups.values())

# time complexity: O(n). space complexity: O(n)
# because no sorting is used for the hashing
def groupAnagramWords2(strs):
    groups = collections.defaultdict(list)
    for s in strs:
        groups[hashkey2(s)].append(s)
    return tuple(groups.values())

print(groupAnagramWords(['abc', 'bcd', 'cba', 'cbd', 'efg']))
# (['abc', 'cba'], ['bcd', 'cbd'], ['efg'])

print(groupAnagramWords2(['abc', 'bcd', 'cba', 'cbd', 'efg']))
# (['abc', 'cba'], ['bcd', 'cbd'], ['efg'])