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
# Output: [[5,4,11,2],[5,8,4,5]]

class Solution:
    def pathSum(self, root, targetSum):
        paths = []
        current = []
        
        self.find_paths(root, targetSum, current, paths)

        return paths
    
    def find_paths(self, root, targetSum, current, paths):
        if root is None:
            return
        
        current.append(root.val)
        if root.val == targetSum and root.left is None and root.right is None:
            paths.append(current)
            return
        
        curr_left = [*current]
        curr_right = [*current]
        
        self.find_paths(root.left, targetSum - root.val, curr_left, paths)
        self.find_paths(root.right, targetSum - root.val, curr_right, paths)

if __name__ == '__main__':
    main = Solution()
    path_sum_result = main.pathSum(a, 22)
    print('path_sum_result:', path_sum_result)