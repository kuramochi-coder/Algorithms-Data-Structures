# Find All Anagrams in a String
# Given two strings s and p, return an array of all the start indices of p's anagrams in s. 
# You may return the answer in any order.


from collections import defaultdict

def find_anagrams(a, b):
    char_map = defaultdict(int)

    # add all characters in b to the char_map, which we will use for comparison
    for c in b:
        char_map[c] += 1

    results = []
    for i in range(len(a)):
        c = a[i] # get char in a

        # remove characters from the char_map as we are sliding it along (sliding window)
        # c_old is the char that is beyond the length of b, so we remove that from char_map by increasing the count by 1
        if i >= len(b):
            c_old = a[i - len(b)]
            char_map[c_old] += 1
            if char_map[c_old] == 0:
                del char_map[c_old]

        # we add characters to char_map by decreasing the count by 1, 
        # so a negative 1 for character 'd' means we seen 'd' in a but it is not in original char_map
        # if char_map of that character is equal to zero then we delete from char_map
        char_map[c] -= 1
        if char_map[c] == 0:
            del char_map[c]

        # if length of char_map is equal to zero, we append the starting index of the anagram to results
        if i + 1 >= len(b) and len(char_map) == 0:
            results.append(i - len(b) + 1)

    return results


print(find_anagrams('acdbacdacb', 'abc'))
# [3, 7]