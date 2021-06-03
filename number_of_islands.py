"""
arr_1 = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
] 
expected output: 1

arr_2 = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
expected output: 3
"""
arr_1 = [["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]
arr_2 = [["1","1","0","0","0"],["1","1","0","0","0"],["0","0","1","0","0"],["0","0","0","1","1"]]

class Solution:
    def numIslands(self, grid):
        if grid is None or len(grid) == 0:
            return 0
        
        number_of_islands = 0
        
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == "1":
                    number_of_islands += self.dfs(grid, i, j)
        
        return number_of_islands
    
    def dfs(self, grid, i, j):
        if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[i]) or grid[i][j] == "0":
            return 0
        
        grid[i][j] = "0"
        
        self.dfs(grid, i + 1, j)
        self.dfs(grid, i - 1, j)
        self.dfs(grid, i, j + 1)
        self.dfs(grid, i, j - 1)
        
        return 1

if __name__ == '__main__':
    main = Solution()
    number_of_islands_result_1 = main.numIslands(arr_1)
    number_of_islands_result_2 = main.numIslands(arr_2)
    print('number_of_islands_result_1:', number_of_islands_result_1)
    print('number_of_islands_result_2:', number_of_islands_result_2)