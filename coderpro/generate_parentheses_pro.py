
class Solution(object):
    def _genParensHelper(self, n, left, right, str):

            if left + right == 2 * n:
                return [str]

            result = []
            if left < n:
                result += self._genParensHelper(n, left + 1, right, str+'(')

            if right < left:
                result += self._genParensHelper(n, left, right + 1, str+')')
            return result

    def genParens(self, n):
        return self._genParensHelper(n, 0, 0, '')


print(Solution().genParens(3))
# ['((()))', '(()())', '(())()', '()(())', '()()()']