arr = [5, 2, 4, 6, 1, 3]

def insertion_sort(A):
    for j in range(1, len(A), 1):
        key = A[j]

        i = j - 1

        # sort ascending when A[i] > key
        while i >= 0 and A[i] > key:
            A[i + 1] = A[i]
            i -= 1
        
        A[i + 1] = key

    return A

if __name__ == '__main__':
    insertion_sort_result = insertion_sort(arr)
    print('insertion_sort_result:', insertion_sort_result)
