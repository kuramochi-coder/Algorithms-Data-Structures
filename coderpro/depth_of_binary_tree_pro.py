
class Node(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def __repr__(self):
        return self.val

class Solution:
    def deepest(self, node):
        if not node:
            return 0
        return 1 + max(self.deepest(node.left), self.deepest(node.right))


    def deepest2(self, node, depth=0):
        if not node:
            return depth + 0

        if not node.left and not node.right:
            return depth + 1

        if not node.left:
            return self.deepest2(node.right, depth + 1)

        if not node.right:
            return self.deepest2(node.left, depth + 1)

        return max(self.deepest2(node.left, depth + 1),
                    self.deepest2(node.right, depth + 1))


#    a
#   / \
#  b   c
# /
# d
#  \
#   e
root = Node('a')
root.left = Node('b')
root.left.left = Node('d')
root.left.left.right = Node('e')
root.right = Node('c')

print(Solution().deepest(root))
# 4
print('---')
print(Solution().deepest2(root))
# 4