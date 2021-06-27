# Cousins in Binary Tree
# In a binary tree, the root node is at depth 0, and children of each depth k node are at depth k+1.
# Two nodes of a binary tree are cousins if they have the same depth, but have different parents.
# We are given the root of a binary tree with unique values, and the values x and y of two different nodes in the tree.
# Return true if and only if the nodes corresponding to the values x and y are cousins.

class Node(object):
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


class Solution(object):
    def _nodes_at_height(self, node, height, exclude):
        if node == None or node == exclude:
            return []
        if height == 0:
            return [node.value]
        return (self._nodes_at_height(node.left, height - 1, exclude) +
                self._nodes_at_height(node.right, height - 1, exclude))

    def _find_node(self, node, target, parent, height):
        if not node:
            return False
        if node == target:
            return (height, parent)
        return (self._find_node(node.left, target, node, height + 1) or
                self._find_node(node.right, target, node, height + 1))

    def list_cousins(self, node, target):
        height, parent = self._find_node(node, target, None, 0)
        return self._nodes_at_height(node, height, parent)

class Solution2:
    def list_cousins(self, node, target):
        queue = [node]

        while len(queue) > 0:
            queue_size = len(queue)
            
            for _ in range(queue_size):
                if target in queue:
                    return [current.value for current in queue if current != target]
                
                current = queue.pop(0)

                if current.left:
                    queue.append(current.left)
                if current.right:
                    queue.append(current.right)

        return False

class Solution3:
    def isCousins(self, root, x, y):
        if not root: return False
        
        queue = [root]
        x_level = 0
        y_level = 0
        curr_level = 0
        
        while(queue):
            curr_level += 1
            queue_size = len(queue)
            
            for _ in range(queue_size):
                node = queue.pop(0)
                if node.value == x: 
                    x_level = curr_level
                if node.value == y: 
                    y_level = curr_level
                    
                if node.left: 
                    queue.append(node.left)
                if node.right: 
                    queue.append(node.right)
                    
                left = node.left.val if node.left else None
                right = node.right.val if node.right else None
                
                if (left == x and right == y) or (left == y and right == x):
                    return False
                
        return x_level == y_level


#     1
#    / \
#   2   3
#  / \    \
# 4   6    5
root = Node(1)
root.left = Node(2)
root.left.left = Node(4)
root.left.right = Node(6)
root.right = Node(3)
root.right.right = Node(5)
print(Solution().list_cousins(root, root.right.right))
# [4, 6]
print(Solution2().list_cousins(root, root.right.right))
# [4, 6]