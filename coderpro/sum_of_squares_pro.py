# Perfect Squares
# Given an integer n, return the least number of perfect square numbers that sum to n.
# A perfect square is an integer that is the square of an integer; in other words, it is the product of some integer with itself. 
# For example, 1, 4, 9, and 16 are perfect squares while 3 and 11 are not.
# Input: n = 13
# Output: 2
# Explanation: 13 = 4 + 9.

def square_sums(n):
    squares = []

    i = 1
    while i*i <= n:
        squares.append(i*i)
        i = i + 1

    min_sums = [n] * (n + 1)
    min_sums[0] = 0

    for i in range(n+1):
        for s in squares:
            if i+s < len(min_sums):
                min_sums[i+s] = min(min_sums[i+s], min_sums[i] + 1)
                
    print(min_sums)
    return min_sums[-1]

print(square_sums(12))
# 3 (Explanation: 12 = 4 + 4 + 4)
print(square_sums(13))
# 2 (Explanation: 13 = 4 + 9)