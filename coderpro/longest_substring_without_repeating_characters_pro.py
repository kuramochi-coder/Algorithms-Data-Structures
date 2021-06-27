# my solution: if letter is seen before, set start and end to same position, reset letters_seen set. 
def lengthOfLongestSubstring2(str):
    letters_seen = set()
    start = 0
    end = 0
    max_length = 0

    while end < len(str):
        c  = str[end]

        if c in letters_seen:
            start =  end
            letters_seen = set()
        
        letters_seen.add(c)

        max_length = max(max_length, end - start + 1)

        end += 1

    return max_length

def lengthOfLongestSubstring(str):
    letter_pos = {}
    start = -1
    end = 0
    max_length = 0

    while end < len(str):
        c = str[end]
        if c in letter_pos:
            start = max(start, letter_pos[c])

        max_length = max(max_length, end - start)

        letter_pos[c] = end
        end += 1
    return max_length

print(lengthOfLongestSubstring2('aabcbbeacfgc'))
print('---')
print(lengthOfLongestSubstring('aabcbbeacfgc'))
# 6