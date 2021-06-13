
class Solution(object):
    def isValid(self, s):

        parentheses = {
            '(': ')',
            '[': ']',
            '{': '}'
        }

        inv_parentheses = {v:k for k,v in parentheses.items()}

        stack = []
        for c in s:
            if c in parentheses:
                stack.append(c)
            elif c in inv_parentheses:
                if len(stack) == 0 or stack[-1] != inv_parentheses[c]:
                    return False
                else:
                    stack.pop()

        return len(stack) == 0

print(Solution().isValid('(){([])}'))
# True

print(Solution().isValid('(){(['))
# False