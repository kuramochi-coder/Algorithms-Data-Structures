import fileinput

input_arr = []

def readInput():
    arr = []
    for line in fileinput.input():
        arr.append(int(line.rstrip()))
    for i in range(1, len(arr)):
        input_arr.append(arr[i])
    
def timeTaken(taps):
    total_time = 0
    total_eff = 0
    for tap in taps:
        total_eff += (1/tap)
    
    total_time = (1 / total_eff) * 60
    
    print(round(total_time))
    
    
readInput()
timeTaken(input_arr)


