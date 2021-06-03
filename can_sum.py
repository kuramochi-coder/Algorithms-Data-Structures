""" 
m = target sum, n = array length
with memoization: time complexity is O(m*n), space complexity is O(m)
without memoization: time complexity is O(n^m), space complexity is O(m) 
"""

def can_sum(target_sum, nums, memo=None):
    # initialize memo if its a new instance
    if memo is None:
        memo = {}

    # we use target_sum as key because nums is not significant to store in memo
    if target_sum in memo:
        return memo[target_sum]

    # base case when zero is reached
    if target_sum == 0:
        return True
    # when we have gone too far and we cannot find a complement
    if target_sum < 0:
        return False
    

    for num in nums:
        remainder = target_sum - num
        if can_sum(remainder, nums, memo):
            memo[target_sum] = True
            return True
    
    memo[target_sum] = False
    return False

""" 
m = target sum, n = array length
without tabulation: time complexity is O(n^m), space complexity is O(m) 
"""
def can_sum_tabulation(target_sum, nums):
    # create table with size of target_sum + 1
    table = [False] * (target_sum + 1)
    table[0] = True
    
    for i in range(target_sum+1):
        if table[i] == True:
            for num in nums:
                if i+num <= target_sum:
                    table[i+num] = True
    
    return table[target_sum]

if __name__ == '__main__':
    # can_sum_result = can_sum(7, [5, 3, 4, 7])
    # print('can_sum_result:', can_sum_result)
    print(can_sum(7, [2, 3])) #True
    print(can_sum(7, [5, 3, 4, 7])) #True
    print(can_sum(7, [2, 4])) #False
    print(can_sum(8, [2, 3, 5])) #True
    print(can_sum(300, [7, 14])) #False
    print('###############################')
    print(can_sum_tabulation(7, [2, 3])) #True
    print(can_sum_tabulation(7, [5, 3, 4, 7])) #True
    print(can_sum_tabulation(7, [2, 4])) #False
    print(can_sum_tabulation(8, [2, 3, 5])) #True
    print(can_sum_tabulation(300, [7, 14])) #False

    