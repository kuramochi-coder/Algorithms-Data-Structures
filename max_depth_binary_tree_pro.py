
class Node(object):
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Note - Recursion won't work on large trees, due to the limit on stack limit size.
# Iteration, on the other hand, uses heap space which is limited only by how
# much memory is in the computer.

class Solution(object):
    def maxDepthBfs(self, n):
        queue = [n]
        depth = 0

        while len(queue) > 0:
            queue_size = len(queue)
            depth += 1
            
            for i in range(queue_size):
                current = queue.pop(0)

                if current.left:
                    queue.append(current.left)
                if current.right:
                    queue.append(current.right)

        return depth

    def maxDepth(self, n):
        stack = [(1, n)]

        max_depth = 0
        while len(stack) > 0:
            depth, node = stack.pop()
            if node:
                max_depth = max(max_depth, depth)
                stack.append((depth + 1, node.left))
                stack.append((depth + 1, node.right))
        return max_depth

    def maxDepthRecursive(self, n):
        if not n:
            return 0
        return max(self.maxDepthRecursive(n.left) + 1,
                self.maxDepthRecursive(n.right) + 1)


n = Node(1)
n.left = Node(2)
n.right = Node(3)
n.left.left = Node(4)

print(Solution().maxDepthBfs(n))
# 3

print(Solution().maxDepth(n))
# 3

print(Solution().maxDepthRecursive(n))
# 3