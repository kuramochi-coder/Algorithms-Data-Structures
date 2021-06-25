

# my solution
def find_permutation2(str1, pattern):
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
  
  return len(result) > 0

def find_permutation(str1, pattern):
  window_start, matched = 0, 0
  char_frequency = {}

  for chr in pattern:
    if chr not in char_frequency:
      char_frequency[chr] = 0
    char_frequency[chr] += 1

  # our goal is to match all the characters from the 'char_frequency' with the current window
  # try to extend the range [window_start, window_end]
  for window_end in range(len(str1)):
    right_char = str1[window_end]
    if right_char in char_frequency:
      # decrement the frequency of matched character
      char_frequency[right_char] -= 1
      if char_frequency[right_char] == 0:
        matched += 1

    if matched == len(char_frequency):
      return True

    # shrink the window by one character
    if window_end >= len(pattern) - 1:
      left_char = str1[window_start]
      window_start += 1
      if left_char in char_frequency:
        if char_frequency[left_char] == 0:
          matched -= 1
        char_frequency[left_char] += 1

  return False


def main():
  print('Permutation exist: ' + str(find_permutation2("oidbcaf", "abc")))
  print('Permutation exist: ' + str(find_permutation2("odicf", "dc")))
  print('Permutation exist: ' + str(find_permutation2("bcdxabcdy", "bcdyabcdx")))
  print('Permutation exist: ' + str(find_permutation2("aaacb", "abc")))

  print('---')

  print('Permutation exist: ' + str(find_permutation("oidbcaf", "abc")))
  print('Permutation exist: ' + str(find_permutation("odicf", "dc")))
  print('Permutation exist: ' + str(find_permutation("bcdxabcdy", "bcdyabcdx")))
  print('Permutation exist: ' + str(find_permutation("aaacb", "abc")))


main()