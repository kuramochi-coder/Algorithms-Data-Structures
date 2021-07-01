# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# a = TreeNode('a')
# b = TreeNode('b')
# c = TreeNode('c')
# d = TreeNode('d')
# e = TreeNode('e')
# f = TreeNode('f')

""" 
        a
    b       c
d       e       f   

expected path for breadth first search: a, b, c, d, e, f
"""

a = TreeNode(3)
b = TreeNode(2)
c = TreeNode(7)
d = TreeNode(4)
e = TreeNode(-2)
f = TreeNode(5)

""" 
        3
    2       7
4       -2       5   
"""

a.left = b
a.right = c
b.left = d
b.right = e
c.right = f

""" 
n: number of nodes in Tree
time complexity is O(n) and space complexity is O(n)
"""

def breadth_first_print(root):
    queue = [root]

    while len(queue) > 0:
        current = queue.pop(0)
        print(current.val)

        if current.left is not None:
            queue.append(current.left)
        if current.right is not None:
            queue.append(current.right)

def breadth_first_search(root, target):
    queue = [root]

    while len(queue) > 0:
        current = queue.pop(0)
        if current.val == target: #target input type is string
            return True

        if current.left is not None:
            queue.append(current.left)
        if current.right is not None:
            queue.append(current.right)
    
    return False

def breadth_first_sum(root):
    queue = [root]
    total_sum = 0

    while len(queue) > 0:
        current = queue.pop(0)
        total_sum += current.val

        if current.left is not None:
            queue.append(current.left)
        if current.right is not None:
            queue.append(current.right)
    
    return total_sum


# breadth_first_print(a)
# print(breadth_first_search(a, "e"))
# print(breadth_first_search(a, "z"))
print(breadth_first_sum(a))