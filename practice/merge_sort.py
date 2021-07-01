arr = [5, 2, 4, 6, 1, 3]

def merge_sort(A):
    if len(A) <= 1:
        return A

    # finding the mid point
    mid = len(A) // 2

    # dividing into 2 parts
    L = A[:mid]
    R = A[mid:]

    # using recursion to combine the left and right
    return merge(A, merge_sort(L), merge_sort(R))
    
    

def merge(A, L, R):

    i = j = k = 0

    # merging L and R arrays in order
    while i < len(L) and j < len(R):
        if L[i] < R[j]:
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            j += 1
        k += 1
    
    # checking if any element was left
    while i < len(L):
        A[k] = L[i]
        i += 1
        k += 1
    while j < len(R):
        A[k] = R[j]
        j += 1
        k += 1

    return A

    

if __name__ == '__main__':
    merge_sort_result = merge_sort(arr)
    print('merge_sort_result:', merge_sort_result)
