""" 
m = target sum, n = array length
without memoization: time complexity is O(n^m * n) and space complexity is O(m^2)
with memoization: time complexity is O(n*m^2) and space complexity is O(m^2)
"""

def best_sum(target_sum, nums, memo=None):
    if memo is None:
        memo = {}
    
    if target_sum in memo:
        return memo[target_sum]

    if target_sum == 0:
        return []
    if target_sum < 0:
        return None

    shortest_combination = None

    for num in nums:
        remainder = target_sum - num
        remainder_array = best_sum(remainder, nums, memo)
        if remainder_array is not None:
            combination = remainder_array + [num]
            if (shortest_combination is None or len(combination) < len(shortest_combination)):
                shortest_combination = combination

    memo[target_sum] = shortest_combination
    return shortest_combination

""" 
m = target sum, n = array length
with tabulation: time complexity is O(n*m^2) and space complexity is O(m^2)
"""
def best_sum_tabulation(target_sum, nums):
    table = [None] * (target_sum + 1)
    table[0] = []

    for i in range(target_sum+1):
        if table[i] is not None:
            for num in nums:
                if i + num <= target_sum:
                    combination = table[i] + [num]
                    if table[i+num] is None or len(combination) < len(table[i+num]):
                        table[i+num] = combination
    
    return table[target_sum]

if __name__ == '__main__':
    print(best_sum(7, [5, 3, 4, 7]))
    print(best_sum(8, [2, 3, 5]))
    print(best_sum(8, [1, 4, 5]))
    print(best_sum(100, [1, 2, 5, 25]))
    print('###############################')
    print(best_sum_tabulation(7, [5, 3, 4, 7]))
    print(best_sum_tabulation(8, [2, 3, 5]))
    print(best_sum_tabulation(8, [1, 4, 5]))
    print(best_sum_tabulation(100, [1, 2, 5, 25]))