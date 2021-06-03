
def sherlockAndAnagrams(s):
    n = len(s)
    word_bank = {}
    pairs_count = 0
    
    for i in range(1, n):
        for j in range(n - i + 1):
            substr = ''.join(sorted(s[j:j+i])) #sorted on s[j:j+i] returns an array ['m', 'o'] so it needs to be joined back to string
            # print(j, j+i, s[j:j+i], sorted(s[j:j+i]))
            word_bank[substr] = word_bank.get(substr, 0) + 1
            # print(substr, word_bank[substr])
            pairs_count += word_bank[substr] - 1

    return pairs_count


print(sherlockAndAnagrams('mom'))