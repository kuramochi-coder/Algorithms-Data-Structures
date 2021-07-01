class Node:
    def __init__(self, value, left=None, right=None, parent=None):
        self.value = value
        self.left = left
        self.right = right
        self.parent = parent

    def __repr__(self):
        return f"({self.value}, {self.left}, {self.right}"


tree = Node(4)
tree.left = Node(2)
tree.right = Node(8)
tree.left.parent = tree
tree.right.parent = tree
tree.left.left = Node(1)
tree.left.left.parent = tree.left
tree.right.right = Node(7)
tree.right.right.parent = tree.right
tree.right.left = Node(5)
tree.right.left.parent = tree.right
tree.right.left.right = Node(7)
tree.right.left.right.parent = tree.right.left
tree.right.right = Node(9)
tree.right.right.parent = tree.right
#     4
#    / \
#   2   8
#  /   / \
# 1   5   9
#      \
#       7

# given a BST (binary search tree) and a node, find the next largest value
def in_order_successor(node):
    # if there is a right child, traverse to that, then keep going left until you get to the end. 
    # that node will have the next largest value
    if node.right:
        curr = node.right
        while curr.left:
            curr = curr.left
        return curr

    # if there is no right child, keep going up to the parent, until there is a left branch.
    # that node will have the next largest value
    curr = node
    parent = curr.parent
    while parent and parent.left != curr:
        curr = parent
        parent = parent.parent
    return parent

print(in_order_successor(tree.right))
# 9

print(in_order_successor(tree.left))
# 4

print(in_order_successor(tree.right.left.right))
# 8