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

# my solution
def find_permutation(str1, pattern):
  start = 0
  char_map = {}
  result = []

  # add all characters in pattern to the hash map
  for s in pattern:
    char_map[s] = char_map.get(s, 0) + 1

  for end in range(len(str1)):
    right_char = str1[end]
    # for every character seen in str1 we decrement the count in the hash map
    char_map[right_char] = char_map.get(right_char, 0) - 1
    if char_map[right_char] == 0:
      del char_map[right_char]

    # slide the window when the number of characters in our sliding window has hit the length limit 
    if end >= len(pattern) - 1:
      # if length of character map is zero then we have matched all the characters in the pattern
      if len(char_map) == 0:
        result.append(start)
      # begin to slide the window by taking note of the character exiting the window
      start_char = str1[start]
      char_map[start_char] = char_map.get(start_char, 0) + 1 # add back the count to the char map when sliding out
      if char_map[start_char] == 0:
        del char_map[start_char]
      start += 1 # slide the window ahead
  
  return result

print(find_anagrams('acdbacdacb', 'abc'))
# [3, 7]

print(find_permutation('acdbacdacb', 'abc'))
# [3, 7]