""" 
with memoization: time complexity is O(m*n), space complexity is O(m+n)
without memoization: time complexity is O(2^m+n), space complexity is O(m +n)
"""
def grid_traveller(m, n, memo=None):
    # initialize memo if its a new instance
    if memo is None:
        memo = {}
        
    # form the key and check if key is in memo
    key = str(m) + ',' + str(n)
    if key in memo:
        return memo[key]
    
    # base case where a 1x1 grid has only 1 way of travel
    if (m == 1 and n ==1):
        return 1
    # another base case where any grid with a 0 is not a grid and has zero ways to travel
    if (m == 0 or n == 0):
        return 0

    # store in memo and return key in memo
    memo[key] = grid_traveller(m -1, n, memo) + grid_traveller(m, n-1, memo)
    return memo[key]

""" 
with tabulation: time complexity is O(m*n), space complexity is O(m+n)
"""
def grid_traveller_tabulation(m, n):
    if m == 0  and n == 0:
        return 0
    """ 
    rows, cols = (5, 5)
    arr = [[0 for i in range(cols)] for j in range(rows)] 
    creating the columns expression: [0 for i in range(cols)], creating the rows expression: for j in range(rows)
    """
    table = [[0 for _ in range(n+1)] for _ in range(m+1)]
    table[1][1] = 1
    
    for i in range(m+1):
        for j in range(n+1):
            current = table[i][j]
            if i + 1 <= m:
                table[i+1][j] += current
            if j + 1 <= n:
                table[i][j+1] += current

    return table[m][n]

if __name__ == '__main__':
    # grid_traveller_result = grid_traveller(18, 18)
    # print('grid_traveller_result:', grid_traveller_result)

    print(grid_traveller(0, 0))
    print(grid_traveller(5, 3))
    print(grid_traveller(18, 18))
    print('---')
    print(grid_traveller_tabulation(0, 0))
    print(grid_traveller_tabulation(5, 3))
    print(grid_traveller_tabulation(18, 18))
