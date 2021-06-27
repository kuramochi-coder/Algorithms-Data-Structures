# Balanced Binary Tree
# Given a binary tree, determine if it is height-balanced.
# For this problem, a height-balanced binary tree is defined as:
# a binary tree in which the left and right subtrees of every node differ in height by no more than 1.
# Input: root = [3,9,20,null,null,15,7]
# Output: true

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def tree_height(self, node):
        if node is None:
            return 0

        heightLeft = self.tree_height(node.left)
        heightRight = self.tree_height(node.right)

        if heightLeft >= 0 and heightRight >= 0 and abs(heightLeft - heightRight) <= 1:
            return max(heightLeft, heightRight) + 1
        return -1


    def is_tree_balanced(self, node):
        return self.tree_height(node) != -1


n4 = Node(4)
n3 = Node(3)
n2 = Node(2, n4)
n1 = Node(1, n2, n3)

#      1
#     / \
#    2   3
#   /
#  4
print(Solution().is_tree_balanced(n1))
# True

n4 = Node(4)
n2 = Node(2, n4)
n1 = Node(1, n2, None)

#      1
#     /
#    2
#   /
#  4
print(Solution().is_tree_balanced(n1))
# False