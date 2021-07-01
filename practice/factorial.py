""" 
n: size if input
time complexity is O(n) and space complexity is O(n)
"""

def factorial(n, memo=None):
    if memo is None:
        memo = {}

    if n in memo:
        return memo[n]

    if n == 1:
        return 1

    memo[n] = n * factorial(n-1, memo)
    return memo[n]

print(factorial(1))
print(factorial(2))
print(factorial(3))
print(factorial(4))
print(factorial(5))
print(factorial(100))