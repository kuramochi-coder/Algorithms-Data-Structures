from collections import defaultdict

class Solution(object):
    def sortColors(self, colors):
        colorsMap = defaultdict(int)
        for c in colors:
            colorsMap[c] += 1

        index = 0
        for i in range(colorsMap[0]):
            colors[index] = 0
            index += 1
        for i in range(colorsMap[1]):
            colors[index] = 1
            index += 1
        for i in range(colorsMap[2]):
            colors[index] = 2
            index += 1

    def sortColor2(self, colors):
        lowIndex = 0
        highIndex = len(colors) - 1
        currIndex = 0

        while currIndex <= highIndex:
            if colors[currIndex] == 0:
                colors[lowIndex], colors[currIndex] = colors[currIndex], colors[lowIndex]
                lowIndex += 1
                currIndex += 1
            elif colors[currIndex] == 2:
                colors[highIndex], colors[currIndex] = colors[currIndex], colors[highIndex]
                highIndex -= 1
            else:
                currIndex += 1

colors = [0, 2, 1, 0, 1, 1, 2]
Solution().sortColors(colors)
print(colors)
# [0, 0, 1, 1, 1, 2, 2]

colors = [0, 2, 1, 0, 1, 1, 2]
Solution().sortColor2(colors)
print(colors)
# [0, 0, 1, 1, 1, 2, 2]
