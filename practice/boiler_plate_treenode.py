# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# root = [1,2,3,None,5,None,4]
a = TreeNode(1)
b = TreeNode(2)
c = TreeNode(3)
d = TreeNode(5)
e = TreeNode(4)

a.left = b
a.right = c
b.right = d
c.right = e
# Output: [1,3,4]