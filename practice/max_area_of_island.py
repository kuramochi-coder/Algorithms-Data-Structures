"""
arr_1 = [   [0,0,1,0,0,0,0,1,0,0,0,0,0],
            [0,0,0,0,0,0,0,1,1,1,0,0,0],
            [0,1,1,0,1,0,0,0,0,0,0,0,0],
            [0,1,0,0,1,1,0,0,1,0,1,0,0],
            [0,1,0,0,1,1,0,0,1,1,1,0,0],
            [0,0,0,0,0,0,0,0,0,0,1,0,0],
            [0,0,0,0,0,0,0,1,1,1,0,0,0],
            [0,0,0,0,0,0,0,1,1,0,0,0,0]
        ]
expected output: 6

arr_2 = [[0,0,0,0,0,0,0,0]]
expected output: 0
"""

arr_1 = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]
arr_2 = [[0,0,0,0,0,0,0,0]]

class Solution:
    def maxAreaOfIsland(self, grid):
        if grid is None or len(grid) == 0:
            return 0
        
        max_area = 0
        
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1:
                    max_area = max(max_area, self.dfs(grid, i, j))
        
        return max_area
    
    def dfs(self, grid, i, j):
        if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[i]) or grid[i][j] == 0:
            return 0
        
        grid[i][j] = 0
        count = 1

        count += self.dfs(grid, i + 1, j)
        count += self.dfs(grid, i - 1, j)
        count += self.dfs(grid, i, j + 1)
        count += self.dfs(grid, i, j - 1)
        
        return count

if __name__ == '__main__':
    main = Solution()
    max_area_of_island_result_1 = main.maxAreaOfIsland(arr_1)
    max_area_of_island_result_2 = main.maxAreaOfIsland(arr_2)
    print('max_area_of_island_result_1:', max_area_of_island_result_1)
    print('max_area_of_island_result_2:', max_area_of_island_result_2)