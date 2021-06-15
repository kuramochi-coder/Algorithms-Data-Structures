# Binary Tree Zigzag Level Order Traversal
# Given the root of a binary tree, return the zigzag level order traversal of its nodes' values. 
# (i.e., from left to right, then right to left for the next level and alternate between).

class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def zigzag_order(node):
    result = []
    currLevel = [node]
    nextLevel = []
    leftToRight = False

    while len(currLevel) > 0:
        node = currLevel.pop()
        result.append(node.value)

        if leftToRight:
            if node.left:
                nextLevel.append(node.left)
            if node.right:
                nextLevel.append(node.right)
        if leftToRight != True:
            if node.right:
                nextLevel.append(node.right)
            if node.left:
                nextLevel.append(node.left)

        if len(currLevel) == 0:
            leftToRight = not leftToRight
            currLevel = nextLevel
            nextLevel = []

    return result


n7 = Node(7)
n6 = Node(6)
n5 = Node(5)
n4 = Node(4)
n3 = Node(3, n6, n7)
n2 = Node(2, n4, n5)
n1 = Node(1, n2, n3)

print(zigzag_order(n1))