""" 
with memoization: time complexity is O(n), space complexity is O(n)
without memoization: time complexity is O(2^n), space complexity is O(n) 
"""
def fib(n, memo=None):
    # initialize memo if its a new instance
    if memo is None:
        memo = {}

    # check if n is in memo
    if n in memo:
        return memo[n]

    # base case where fib(1) == 1 and fib(2) == 1
    if (n == 1 or n == 2):
        return 1
    
    if n == 0:
        return 0

    # store in memo and return key in memo
    memo[n] = fib(n -1, memo) + fib(n - 2, memo)
    return memo[n]
    
""" 
with tabulation: time complexity is O(n), space complexity is O(n) 
"""
def fib_tabulation(n):
    if n == 0:
        return 0

    table = [0] * (n+1)
    table[1] = 1
    
    for i in range(2, n + 1):
        # we have result of i-1 and i-2 available because these had been evaluated already
        table[i] = table[i - 1] + table[i - 2]
        # return the value of n in tabulation table

    return table[n]

# from tech interview pro
def fibIterative(n):
    stack = []
    stack.append(n)
    sum = 0

    while(len(stack) > 0):
      n = stack.pop()
      if n == 0:
        sum += 0
      elif n == 1:
        sum +=1
      else:
        stack.append(n-1)
        stack.append(n-2)

    return sum

if __name__ == '__main__':
    # fibo_result = fib(6)
    # print('fibo_result:', fibo_result)
    print(fib(6))
    print('--')
    print(fib_tabulation(6))
    print('--')
    print(fibIterative(6))