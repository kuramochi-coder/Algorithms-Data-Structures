# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# root = [5,4,8,11,null,13,4,7,2,null,null,null,1], targetSum = 22
a = TreeNode(5)
b = TreeNode(4)
c = TreeNode(8)
d = TreeNode(11)
e = TreeNode(13)
f = TreeNode(4)
g = TreeNode(7)
h = TreeNode(2)
i = TreeNode(1)
j = TreeNode(5)

a.left = b
a.right = c
b.left = d
c.left = e
c.right = f
d.left = g
d.right = h
f.left = j
f.right = i
# Output: True

class Solution:
    def hasPathSum(self, root, targetSum):
        if root is None:
            return False
        elif root.left is None and root.right is None and targetSum - root.val == 0:
            return True
        else:
            return self.hasPathSum(root.left, targetSum - root.val) or self.hasPathSum(root.right, targetSum - root.val)

if __name__ == '__main__':
    main = Solution()
    has_path_sum_result = main.hasPathSum(a, 22)
    print('has_path_sum_result:', has_path_sum_result)