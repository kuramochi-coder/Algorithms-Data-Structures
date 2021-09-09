# return list of fibonacci numbers


def fib(n, memo=None):
    if memo is None:
        memo = {}

    if n in memo:
        return memo[n]

    result = []

    if n == 1:
        return [0]

    if n == 2:
        return [0, 1]

    result = fib(n - 1)
    result.append(result[-1] + result[-2])
    memo[n] = result
    return memo[n]


# liliabloch@yahoo.com

0, 1, 1, 2, 3, 5, 8, 13
print(fib(30))