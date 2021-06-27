
class Node(object):
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
  # return value (isBalanced, height)
    def _is_balanced_helper(self, n):
        if not n:
            return (True, 0)

        lBalanced, lHeight = self._is_balanced_helper(n.left)
        rBalanced, rHeight = self._is_balanced_helper(n.right)
        return (lBalanced and rBalanced and abs(lHeight - rHeight) <= 1,
                max(lHeight, rHeight) + 1)

    def is_balanced(self, n):
        return (self._is_balanced_helper(n)[0], self._is_balanced_helper(n)[1])


n = Node(1)
n.left = Node(2)
n.left.left = Node(4)
n.right = Node(3)
#    1
#   / \
#  2   3
# /
#4
print(Solution().is_balanced(n))

n.right = None
#    1
#   /
#  2
# /
#4
print(Solution().is_balanced(n))
# False