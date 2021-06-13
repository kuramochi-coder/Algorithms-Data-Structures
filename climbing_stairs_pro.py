# this is essentially the Fibonacci solution

def staircase(n, memo=None):
    if memo is None:
        memo = {}
    
    if n in memo:
        return memo[n]

    if n <= 1:
        return 1

    memo[n] = staircase(n-1, memo) + staircase(n-2, memo)
    return memo[n]

def staircase2(n):
    if (n <= 1):
        return 1

    prev = 1
    prevprev = 1
    curr = 0

    for i in range(2, n + 1):
        curr = prev + prevprev

        prevprev = prev
        prev = curr
    return curr


print(staircase(5))
# 8

print(staircase2(5))
# 8