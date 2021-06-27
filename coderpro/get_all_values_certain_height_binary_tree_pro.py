
class Node():
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def valuesAtLevel(node, depth):
    if not node:
        return []

    if depth == 1:
        return [node.value]

    return valuesAtLevel(node.left, depth - 1) + valuesAtLevel(node.right, depth - 1)

def valuesAtLevelIterative(node, depth):
    queue = [node]
    current_level = 0
    result = []

    while len(queue) > 0:
        queue_size = len(queue)
        current_level += 1
        
        for i in range(queue_size):
            current = queue.pop(0)

            if current_level == depth:
                result.append(current.value)
            
            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)
        
    return result



#    1
#   / \
#  2   3
# / \   \
# 4   5   7
node = Node(1)
node.left = Node(2)
node.right = Node(3)
node.right.right = Node(7)
node.left.left = Node(4)
node.left.right = Node(5)

print(valuesAtLevel(node, 3))
# [ 4, 5, 7]

print(valuesAtLevelIterative(node, 3))
# [ 4, 5, 7]