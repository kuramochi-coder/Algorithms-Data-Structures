# Binary Tree Zigzag Level Order Traversal
# Given the root of a binary tree, return the zigzag level order traversal of its nodes' values. 
# (i.e., from left to right, then right to left for the next level and alternate between).

class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

class Solution:
    def zigzag_order(self, node):
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

class Solution2:
    def zigzagLevelOrder(self, root):
        if root is None:
            return []
            
        queue = [root]
        current_level = 0

        result = []
        while len(queue) > 0:
            queue_size = len(queue)
            current_level += 1
            level_list = []

            for i in range(queue_size):
                current = queue.pop(0)

                level_list.append(current.value)
                
                if current.left:
                    queue.append(current.left)
                if current.right:
                    queue.append(current.right)

            if current_level % 2 == 0:
                result.append(level_list)
            else:
                result.append(level_list[::-1])
        
        return result

            





n7 = Node(7)
n6 = Node(6)
n5 = Node(5)
n4 = Node(4)
n3 = Node(3, n6, n7)
n2 = Node(2, n4, n5)
n1 = Node(1, n2, n3)

print(Solution().zigzag_order(n1))
# [1, 2, 3, 7, 6, 5, 4]
print(Solution2().zigzagLevelOrder(n1))
# [1, 2, 3, 7, 6, 5, 4]