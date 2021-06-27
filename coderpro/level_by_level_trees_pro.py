
from collections import deque

class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children

def levelPrint(node):
    q = deque([node])
    result = ''
    while len(q):
        num = len(q)
        while num > 0:
            node = q.popleft()
            result += str(node.val)
            for child in node.children:
                q.append(child)
            num -= 1
        result += "\n"
    return result

def levelPrint2(node):
    queue = [node]
    result = ''

    while len(queue) > 0:
        queue_size = len(queue)

        for i in range(queue_size):
            current =  queue.pop(0)

            result += current.val

            if current.children:
                for child in current.children:
                    queue.append(child)
        
        result += '\n'
    
    return result

tree = Node('a', [])
tree.children = [Node('b', []), Node('c', [])]
tree.children[0].children = [Node('g', [])]
tree.children[1].children = [Node('d', []), Node('e', []), Node('f', [])]

print(levelPrint(tree))
# a
# bc
# gdef
print('---')
print(levelPrint2(tree))