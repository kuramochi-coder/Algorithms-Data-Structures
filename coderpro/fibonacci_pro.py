
def fib(n):
    a = 0
    b = 1
    if n == 0:
        return a
    if n == 1:
        return b

    for _ in range(2, n+1):
        value = a + b

        a = b
        b = value
    return value


print(fib(10))
# 55