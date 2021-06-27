""" 
m = target sum, n = array length
without memoization: time complexity is O(n^m * n) and space complexity is O(m)
with memoization: time complexity is O(n*m^2) and space complexity is O(m^2)
"""
def how_sum(target_sum, nums, memo=None):
    if memo is None:
        memo = {}

    if target_sum in memo:
        return memo[target_sum]
    if target_sum == 0:
        return []
    if target_sum < 0:
        return None

    for num in nums:
        remainder = target_sum - num
        remainder_combination = how_sum(remainder, nums, memo)
        if remainder_combination is not None:
            result_combination = remainder_combination + [num]
            memo[target_sum] = result_combination
            return result_combination

    
    memo[target_sum] = None
    return None

""" 
m = target sum, n = array length
with tabulation: time complexity is O(n*m^2) and space complexity is O(m^2)
"""
def how_sum_tabulation(target_sum, nums):
    table = [None] * (target_sum + 1)
    table[0] = []

    for i in range(target_sum+1):
        if table[i] is not None:
            for num in nums:
                if i + num <= target_sum:
                    table[i+num] = table[i] + [num]
    
    return table[target_sum]
    
if __name__ == '__main__':
    print(how_sum(7, [2, 3]))
    print(how_sum(7, [5, 3, 4, 7]))
    print(how_sum(7, [2, 4]))
    print(how_sum(8, [2, 3, 5]))
    print(how_sum(300, [7, 14]))
    print('###############################')
    print(how_sum_tabulation(7, [2, 3]))
    print(how_sum_tabulation(7, [5, 3, 4, 7]))
    print(how_sum_tabulation(7, [2, 4]))
    print(how_sum_tabulation(8, [2, 3, 5]))
    print(how_sum_tabulation(300, [7, 14]))