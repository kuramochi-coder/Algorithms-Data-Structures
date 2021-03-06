# String Anagrams (hard)
# Given a string and a pattern, find all anagrams of the pattern in the given string.

# Every anagram is a permutation of a string. As we know, when we are not allowed to repeat characters while finding permutations of a string, we get N!N! permutations (or anagrams) of a string having NN characters. For example, here are the six anagrams of the string “abc”:

# abc
# acb
# bac
# bca
# cab
# cba
# Write a function to return a list of starting indices of the anagrams of the pattern in the given string.

# Example 1:
# Input: String="ppqp", Pattern="pq"
# Output: [1, 2]
# Explanation: The two anagrams of the pattern in the given string are "pq" and "qp".

# my solution
def find_string_anagrams2(str1, pattern):
  result_indexes = []
  start = 0
  char_map = {}

  for c in pattern:
    char_map[c] = char_map.get(c, 0) + 1

  for end in range(len(str1)):
    right_char = str1[end]

    char_map[right_char] = char_map.get(right_char, 0) - 1
    if char_map[right_char] == 0:
      del char_map[right_char]

    if end >= len(pattern) - 1:
      if len(char_map) == 0:
        result_indexes.append(start)

      left_char = str1[start]
      
      char_map[left_char] = char_map.get(left_char, 0) + 1
      if char_map[left_char] == 0:
        del char_map[left_char]

      start += 1  
     
  return result_indexes


def find_string_anagrams(str1, pattern):
  window_start, matched = 0, 0
  char_frequency = {}

  for chr in pattern:
    if chr not in char_frequency:
      char_frequency[chr] = 0
    char_frequency[chr] += 1

  result_indices = []
  # Our goal is to match all the characters from the 'char_frequency' with the current window
  # try to extend the range [window_start, window_end]
  for window_end in range(len(str1)):
    right_char = str1[window_end]
    if right_char in char_frequency:
      # Decrement the frequency of matched character
      char_frequency[right_char] -= 1
      if char_frequency[right_char] == 0:
        matched += 1

    if matched == len(char_frequency):  # Have we found an anagram?
      result_indices.append(window_start)

    # Shrink the sliding window
    if window_end >= len(pattern) - 1:
      left_char = str1[window_start]
      window_start += 1
      if left_char in char_frequency:
        if char_frequency[left_char] == 0:
          matched -= 1  # Before putting the character back, decrement the matched count
        char_frequency[left_char] += 1  # Put the character back

  return result_indices


def main():
  print(find_string_anagrams("ppqp", "pq"))
  print(find_string_anagrams("abbcabc", "abc"))


main()
