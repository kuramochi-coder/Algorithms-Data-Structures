
class Solution(object):
    def num_islands(self, grid):
        if not grid or not grid[0]:
            return 0
        numRows, numCols = len(grid), len(grid[0])
        count = 0

        for row in range(numRows):
            for col in range(numCols):
                if self._is_land(grid, row, col):
                    count += 1
                    self._sinkLand(grid, row, col)
        return count

    def _sinkLand(self, grid, row, col):
        if not self._is_land(grid, row, col):
            return
        grid[row][col] = 0
        for d in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            self._sinkLand(grid, row + d[0], col + d[1])

    def _is_land(self, grid, row, col):
        if row < 0 or col < 0 or row >= len(grid) or col >= len(grid[0]):
            return False
        return grid[row][col] == 1

grid = [[1, 1, 0, 0, 0],
        [0, 1, 0, 0, 1],
        [1, 0, 0, 1, 1],
        [0, 0, 0, 0, 0]]

print(Solution().num_islands(grid))
# 3