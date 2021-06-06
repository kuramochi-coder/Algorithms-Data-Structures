# Rotate List
# Given the head of a linked list, rotate the list to the right by k places.
# Input: head = [1,2,3,4,5], k = 2
# Output: [4,5,1,2,3]

class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def __repr__(self):
        # return f"({self.value}, {self.next})"
        n = self
        ret = ''
        while n:
            ret += str(n.value) + ' '
            n = n.next
        return ret

def rotate(node, n):
    length = 0
    curr = node
    while curr != None:
        curr = curr.next
        length +=1
    n = n % length

    slow, fast = node, node
    for i in range(n):
        fast = fast.next

    while fast.next != None:
        slow = slow.next
        fast = fast.next

    fast.next = node
    head = slow.next
    slow.next = None

    return head

node = Node(1, Node(2, Node(3, Node(4, Node(5)))))

print(rotate(node, 2))
# 4, 5, 1, 2, 3