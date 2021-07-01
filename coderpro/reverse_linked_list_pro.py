
class Node(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        res = str(self.val)
        if self.next:
            res += str(self.next)
        return res

class Solution(object):
    def reverse(self, node):
        curr = node
        prev = None

        while curr != None:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp

        return prev

node = Node(1, Node(2, Node(3, Node(4, Node(5)))))

print(Solution().reverse(node))
# 54321