import fileinput
import sys

arr = []
input_arr = []
k = []

def readInput():
    for line in fileinput.input():
        arr.append(line.rstrip())
    
    k.append(int(arr[0].split(sep=" ")[1]))
    for i in range(1, len(arr)):
        input_arr.append(arr[i].split(sep=" "))
        
def optimalSelection(names, k):
    names.sort(key=lambda x: (int(x[1]), x[0]))
    total_count = 0
    # print(names)
    
    # min_sum , window_sum = float('inf'), 0
    # window_start = 0
    selected_names = []

#     for window_end in range(len(names)):
          
#         split_name = names[window_end][0].split(sep = '+')
#         unique_name = split_name[0]
#         is_partner = int(split_name[1])
#         print(unique_name)
#         print(is_partner)
#         if unique_name not in selected_names and is_partner != 1:
#             selected_names.append(unique_name)
#             window_sum += int(names[window_end][1])
#         # slide the window, we don't need to slide if we've not hit the required window size of 'k'
#         if window_end >= k-1:
#           min_sum = min(min_sum, window_sum)
#           window_sum -= int(names[window_start][1])  # subtract the element going out
#           window_start += 1  # slide the window ahead

    while len(selected_names) != k:
        full_name, count = names.pop(0)
        full_name = full_name.split(sep = '+')
        unique_name = full_name[0]
        if len(full_name) > 1:
            is_partner = int(full_name[1])
        else:
            is_partner = 0
        # print(unique_name)
        # print(is_partner)
        
        if selected_names and unique_name not in selected_names and is_partner:
            continue
        else:
            selected_names.append(unique_name)
            total_count += int(count) 
    # print(selected_names)
    print(total_count)

readInput()
optimalSelection(input_arr, k[0])