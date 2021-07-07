import fileinput

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
            
    for i in range(len(result)):
        for j in range(i):
            print('+ ')
        print('\n')
   
        
    
    
        
            
# readInput()
# print(input_arr)
barChart(input_arr)

        