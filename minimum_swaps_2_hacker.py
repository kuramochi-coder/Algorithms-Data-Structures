
def minimumSwaps(arr):
    swap_count = 0
    
    for i in range(len(arr)):
        correct_value = i + 1
        while arr[i] != correct_value:
            element_value = arr[i]
            arr[element_value - 1], arr[i] = arr[i], arr[element_value - 1]
            swap_count += 1 
    
    return swap_count

def minimumSwapsForLoop(arr):
    swap_count = 0
    
    for i in range(len(arr)):
        correct_value = i + 1
        if arr[i] != correct_value:
            original_value = arr[i]
            for j in range(i+1, len(arr)):
                if arr[j] == correct_value:
                    arr[i] = correct_value
                    arr[j] = original_value
                    swap_count += 1
                    break
    
    return swap_count

def minimumSwapsUp(arr):
    swap_count = 0
    
    for i in range(len(arr)):
        correct_value = i + 1
        if arr[i] != correct_value:
            start = i + 1
            while start < len(arr) and arr[start] != correct_value:
                start += 1
            arr[i], arr[start] = arr[start], arr[i]
            swap_count += 1
    
    return swap_count

def minimumSwapsDown(arr):
    swap_count = 0
    
    for i in range(len(arr)-1, -1, -1):
        correct_value = i + 1
        if arr[i] != correct_value:
            start = i + 1
            while start >= 0 and arr[start] != correct_value:
                start -= 1
            arr[i], arr[start] = arr[start], arr[i]
            swap_count += 1
    
    return swap_count

print(minimumSwaps([4, 3, 1, 2]))
# 3

print(minimumSwaps([1, 3, 5, 2, 4, 6, 7]))
# 3