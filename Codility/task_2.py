def solution(K, A):
    # write your code in Python 3.6
    # pass

    if A is None or len(A) == 0:
        return 0


    number_of_stores = 0

    for i in range(len(A)):
        for j in range(len(A[i])):
            if A[i][j] == 0:
                number_of_stores = max(number_of_stores, dfs(K, A, i, j))

    return number_of_stores

def dfs(K, A, i, j):
    if i < 0 or i >= len(A) or j < 0 or j >= len(A[i]) or A[i][j] == 1:
        return 0

    A[i][j] = 1
    count = 1

    count += min(K, dfs(K, A, i+1, j))
    count += min(K, dfs(K, A, i-1, j))
    count += min(K, dfs(K, A, i, j+1))
    count += min(K, dfs(K, A, i, j-1))  

    return count