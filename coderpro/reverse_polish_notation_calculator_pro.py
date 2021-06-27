def calc(inputs):
    stack = []

    for i in inputs:
        if i in ('-', '+', '*', '/'):
            b = stack.pop()
            a = stack.pop()
            if i == '-':
                stack.append(a - b)
            if i == '+':
                stack.append(a + b)
            if i == '*':
                stack.append(a * b)
            if i == '/':
                stack.append(a / b)
        else:
            stack.append(i)
    return stack[0]

print(calc([1, 2, 3, '+', 2, '*', '-']))