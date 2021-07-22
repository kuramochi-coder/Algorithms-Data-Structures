import fileinput
import numpy as np

input_arr = [[3, 1, 2], [5, 2, 3]]

def readInput():
    for line in fileinput.input():
        input_arr.append([int(num) for num in line.rstrip() if num.isnumeric()])
    
def barChart(points):
    cols = len(points[0])
    result = [0] * cols
    points_result = []
    
    for i in range(len(points)):
        for j in range(len(points[0])):
            result[j] = max(result[j], points[i][j])

    print(result)
            
    # for i in range(len(result)):
    #     for j in range(result[i]):
    #         print('+ ', end='')
    #     print('')

    result_array = []
    for i in range(len(result)):
        currentstring = ''
        for j in range(result[i]):
            currentstring += '+'
        result_array.append(currentstring)

        print(currentstring)
    print(result_array)
    
    # arr1 = np.array(result_array)

    # print(f'Original Array:\n{arr1}')

    # arr1_transpose = arr1.transpose()

    # print(f'Transposed Array:\n{arr1_transpose}')
    

   
        
    
    
        
            
# readInput()
# print(input_arr)
barChart(input_arr)

        