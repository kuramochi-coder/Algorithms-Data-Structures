# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

arr = [2, 6, 8, 5]
arr_2 = [1, 5, 5, 2, 6]
arr_3 = [1, 1]

def solution(blocks):
    # write your code in Python 3.6
    # pass

    if len(blocks) == 2 or sum(blocks) == 0:
        return len(blocks) 

    max_sum = None
    start = None
    max_distance = 0 
    i = 0

    while i < len(blocks) -1:
        while i-1 >=0 and i < len(blocks) and blocks[i-1] == blocks[i]:
            i -= 1
        
        start = i

        down_sum = 0

        while i+1 < len(blocks) and blocks[i+1] <= blocks[i]:
            down_sum += blocks[i]
            i += 1
        
        up_sum = 0

        while i+1 < len(blocks) and blocks[i+1] >= blocks[i]:
            up_sum += blocks[i]
            i += 1
        
        total_sum = up_sum + down_sum

        if max_sum is None or total_sum > max_sum:
            max_sum = total_sum
            max_distance = i - start + 1
    
    return max_distance

print(solution(arr_3))