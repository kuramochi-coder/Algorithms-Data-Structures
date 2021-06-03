
class Solution:
    def sockMerchant(self, ar):
        hash_map = {}
        count = 0
        
        for num in ar:
            hash_map[num] = hash_map.get(num, 0) + 1
                
        for key in hash_map:
            count += hash_map[key] // 2 
            
        return count

print(Solution().sockMerchant([10, 20, 20, 10, 10, 30, 50, 10, 20]))
# output 3