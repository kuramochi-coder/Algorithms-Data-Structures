# Prison Cells After N Days
# There are 8 prison cells in a row and each cell is either occupied or vacant.

# Each day, whether the cell is occupied or vacant changes according to the following rules:

# If a cell has two adjacent neighbors that are both occupied or both vacant, then the cell becomes occupied.
# Otherwise, it becomes vacant.
# Note that because the prison is a row, the first and the last cells in the row can't have two adjacent neighbors.

# You are given an integer array cells where cells[i] == 1 if the ith cell is occupied and cells[i] == 0 if the ith cell is vacant, and you are given an integer n.

# Return the state of the prison after n days (i.e., n such changes described above).

# Example 1:

# Input: cells = [0,1,0,1,1,0,0,1], n = 7
# Output: [0,0,1,1,0,0,0,0]
# Explanation: The following table summarizes the state of the prison on each day:
# Day 0: [0, 1, 0, 1, 1, 0, 0, 1]
# Day 1: [0, 1, 1, 0, 0, 0, 0, 0]
# Day 2: [0, 0, 0, 0, 1, 1, 1, 0]
# Day 3: [0, 1, 1, 0, 0, 1, 0, 0]
# Day 4: [0, 0, 0, 0, 0, 1, 0, 0]
# Day 5: [0, 1, 1, 1, 0, 1, 0, 0]
# Day 6: [0, 0, 1, 0, 1, 1, 0, 0]
# Day 7: [0, 0, 1, 1, 0, 0, 0, 0]

class Solution:
    def prisonAfterNDays(self, cells, n):
        if n == 0: return cells
        if n > 14: n = (n-1) % 14 + 1 # there is a repetitive pattern after every 14 rounds

        for _ in range(n):
            ones = []
            zeroes = []
            for i in range(1, len(cells) - 1):
                if (cells[i-1] == 0 and cells[i+1] == 0) or (cells[i-1] == 1 and cells[i+1] == 1):
                    ones.append(i)
                else:
                    zeroes.append(i)
                    
            for index in ones: cells[index] = 1
            for index in zeroes: cells[index] = 0
            cells[0] = cells[-1] = 0
            
        return cells

print(Solution().prisonAfterNDays([0,1,0,1,1,0,0,1], 7))
# [0,0,1,1,0,0,0,0]