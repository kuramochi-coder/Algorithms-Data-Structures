# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


a = TreeNode('a')
b = TreeNode('b')
c = TreeNode('c')
d = TreeNode('d')
e = TreeNode('e')
f = TreeNode('f')

a.left = b
a.right = c
b.left = d
b.right = e
c.right = f

""" 
        a
    b       c
d       e       f   

expected path for depth first search: a, b, d, e, c, f
"""

""" 
n: number of nodes in Tree
time complexity is O(n) and space complexity is O(n)
"""
def depth_first_print_iterative(root):
    stack = [root]

    while len(stack) > 0:
        current = stack.pop(-1)
        print(current.val)

        if current.right is not None:
            stack.append(current.right)
        if current.left is not None:
            stack.append(current.left)

# pre-order traversal: traverse parent before the children
def depth_first_print_recursive(root):
    # base case
    if root is None:
        return
    
    print(root.val)
    depth_first_print_recursive(root.left)
    depth_first_print_recursive(root.right)



# depth_first_print_iterative(a)
depth_first_print_recursive(a)