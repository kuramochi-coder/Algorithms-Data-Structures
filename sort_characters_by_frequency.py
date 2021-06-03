s_1 = "tree"
s_2 = "cccaaa"

class Solution:
    def frequencySort(self, s: str) -> str:
        hash_map = {}
        result = ''

        for char in s:
            if char in hash_map:
                hash_map[char] += 1
            else:
                hash_map[char] = 1

        s = sorted(hash_map, key=lambda x: hash_map[x], reverse=True)
        
        for char in s:
            result += char * hash_map[char]

        return result

if __name__ == '__main__':
    main = Solution()
    sorted_result_1 = main.frequencySort(s_1)
    sorted_result_2 = main.frequencySort(s_2)
    print('sorted_result_1:', sorted_result_1)
    print('sorted_result_2:', sorted_result_2)