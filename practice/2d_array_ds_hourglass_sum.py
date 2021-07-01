
class Solution:
    def hourglassSum(self, arr):
        max_sum = None
        
        for y in range(len(arr)):
            for x in range(len(arr[y])):
                current_sum = 0
                if x + 2 < len(arr[y]) and y + 2 < len(arr):
                    current_sum += arr[y][x] + arr[y][x+1] + arr[y][x+2] + arr[y+1][x+1] + arr[y+2][x] + arr[y+2][x+1] + arr[y+2][x+2]
                    if max_sum is None:
                        max_sum = current_sum
                    else:
                        max_sum = max(max_sum, current_sum)
        
        return max_sum

matrix = [
    [1, 1, 1, 0, 0, 0],
    [0, 1, 0, 0, 0, 0],
    [1, 1, 1, 0, 0, 0],
    [0, 0, 2, 4, 4, 0],
    [0, 0, 0, 2, 0, 0],
    [0, 0, 1, 2, 4, 0]
]
print(Solution().hourglassSum(matrix))
# Expected Output: 19

matrix = [
    [-9, -9, -9, 1, 1, 1],
    [0, -9, 0, 4, 3, 2],
    [-9, -9, -9, 1, 2, 3],
    [0, 0, 8, 6, 6, 0],
    [0, 0, 0, -2, 0, 0],
    [0, 0, 1, 2, 4, 0]
]
print(Solution().hourglassSum(matrix))
# Expected Output: 28

