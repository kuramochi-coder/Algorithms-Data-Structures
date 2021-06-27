
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        result = ''
        result += str(self.val)
        if self.left:
            result += str(self.left)
        if self.right:
            result += str(self.right)
        return result

# pre-order traversal 
def serialize(node):
    if node == None:
        return '#'
    return str(node.val) + ' ' + serialize(node.left) + ' ' + serialize(node.right)

def deserialize(str):
    values = iter(str.split())
    return deserialize_helper(values)

def deserialize_helper(values):
    value = next(values)
    if value == '#':
        return None
    node = Node(int(value))
    node.left = deserialize_helper(values)
    node.right = deserialize_helper(values)
    return node
    


#      1
#     / \
#    3   4
#   / \   \
#  2   5   7
tree = Node(1)
tree.left = Node(3)
tree.right = Node(4)
tree.left.left = Node(2)
tree.left.right = Node(5)
tree.right.right = Node(7)
string = serialize(tree)
print(tree)
print('---')
print(string)
print('---')
print(deserialize(string))
# 132547