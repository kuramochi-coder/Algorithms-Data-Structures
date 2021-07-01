""" 1, 2, 3, 4, 5, 6, 7, 8

    1, 2, 3, 4, 5, 8, 6, 7  """

class Solution:
    def minimumBribes(self, q):
        total_bribes = 0
        
        for i in range(len(q)-1, -1, -1):
            if q[i] != i + 1:
                if q[i - 1] == i + 1:
                    total_bribes += 1
                    q[i], q[i - 1] = q[i - 1], q[i]
                elif q[i - 2] == i + 1:
                    total_bribes += 2
                    q[i], q[i - 1], q[i - 2] = q[i - 2], q[i], q[i - 1] #look at example above to visualize swap of 8 back to original
                else:
                    print('Too chaotic')
                    return
                
        print(total_bribes)

Solution().minimumBribes([2, 1, 5, 3, 4])
# 3

Solution().minimumBribes([2, 5, 1, 3, 4])
# Too chaotic