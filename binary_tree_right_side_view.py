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

class Solution:
    def rightSideView(self, root: TreeNode):
        if root is None:
            return []
        
        queue = [root]
        
        right_side_view = []
        
        while len(queue) > 0:
            queue_size = len(queue)
            
            for i in range(queue_size):
                current = queue.pop(0)
                
                if i == queue_size - 1:
                    right_side_view.append(current.val)

                if current.left is not None:
                    queue.append(current.left)
                if current.right is not None:
                    queue.append(current.right)
        
        return right_side_view

if __name__ == '__main__':
    main = Solution()
    right_side_view_result_1 = main.rightSideView(a)
    print('right_side_view_result_1:', right_side_view_result_1)