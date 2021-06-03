
class Solution:
    def reconstructQueue(self, input):
        input.sort(key=lambda x:
                (-x[0], x[1])
                )
        # [[7, 0], [7, 1], [6, 1], [5, 0], [5, 2], [4, 4]] after sorting by x[0] largest to smallest
        res = []
        for person in input:
            res.insert(person[1], person)
        return res

    def reconstructQueue2(self, input):
        input = sorted(input, key=lambda x: (-x[0], x[1]))
        # [[7, 0], [7, 1], [6, 1], [5, 0], [5, 2], [4, 4]] after sorting by x[0] largest to smallest
        res = []
        for person in input:
            res.insert(person[1], person)
        return res


input = [[7, 0], [4, 4], [7, 1], [5, 0], [6, 1], [5, 2]]
print(Solution().reconstructQueue(input))
print(Solution().reconstructQueue2(input))