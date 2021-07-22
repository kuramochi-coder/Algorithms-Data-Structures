# Problem is to count the amount of water that can be stored in the valleys

x = [3, 0, 2, 0, 4]

def brute_force(arr):
    result = 0

    for i in range(len(arr)):
        left =  arr[i]

        for j in range(i):
            left = max(left, arr[j])

        right = arr[i]

        for j in range(i+1, len(arr)):
            right = max(right, arr[j])

        result += min(left, right) - arr[i]

    return result

print(brute_force(x))

def optimise(arr):
    L = 0
    R = len(arr) -1
    left_max, right_max = 0, 0
    result = 0

    while L < R:
        left_max = max(left_max, arr[L])

        right_max = max(right_max, arr[R])

        if right_max > left_max:
            result += max(0, left_max - arr[L])
            L += 1
        else:
            result += max(0, right_max - arr[R])
            R -= 1

    
    return result

print(optimise(x))

        

        


