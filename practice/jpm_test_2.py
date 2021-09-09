# class A(object):
#     x = 1

# class B(A):
#     pass

# class C(A):
#     pass

# # print(B.x)
# # print(C.x)

# B.x = 2
# A.x = 3

# print(A.x)
# print(B.x)
# print(C.x)

# def new(arr):
# result = ""

# for s in arr:
#     result += s

# return f'{result} {result} {result}'

# arr_length = len(arr)
# arr.append(arr_length)

# return arr

# print(new())
# arr1 = ['A', 'B', 'C']
# arr2 = []
# ABC ABC ABC
# [A,B,C,3]

# print(new(arr1))

# Table A
# col1
# 1
# 2
# 4

# Table B
# col2
# 2
# 1
# 5
# null

# select *
# from Table A inner join Table B on A.col1 = B.col2


def fib(n):
    result = []

    if n == 1:
        return [0]

    if n == 2:
        return [0, 1]

    result = fib(n - 1)
    result.append(result[-1] + result[-2])
    return result


# liliabloch@yahoo.com

0, 1, 1, 2, 3, 5, 8
print(fib(8))