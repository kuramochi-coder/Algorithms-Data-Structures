from collections import defaultdict


def find_anagrams(a, b):
    # char_map = defaultdict(int)
    char_map = {}

    for c in b:
        # char_map[c] += 1
        char_map[c] = char_map.get(c, 0) + 1
    # print(char_map)

    results = []
    for i in range(len(a)):
        c = a[i]

        if i >= len(b):
            c_old = a[i - len(b)]
            # char_map[c_old] += 1
            char_map[c_old] = char_map.get(c_old, 0) + 1
            if char_map[c_old] == 0:
                del char_map[c_old]

        # char_map[c] -= 1
        char_map[c] = char_map.get(c, 0) - 1
        if char_map[c] == 0:
            del char_map[c]

        if i + 1 >= len(b) and len(char_map) == 0:
            results.append(i - len(b) + 1)

    return results


print(find_anagrams('acdbacdacb', 'abc'))
# [3, 7]