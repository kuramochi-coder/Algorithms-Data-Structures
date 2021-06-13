# Swap Nodes in Pairs
# Given a linked list, swap every two adjacent nodes and return its head. You must solve the problem without modifying the values in the list's nodes (i.e., only nodes themselves may be changed.)
# Input: head = [1,2,3,4]
# Output: [2,1,4,3]
 

class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def __repr__(self):
        return f"{self.value}, ({self.next.__repr__()})"


def swap_every_two(node):
    curr = node
    while curr != None and curr.next != None:
        curr.value, curr.next.value = curr.next.value, curr.value
        curr = curr.next.next
    return node


node = Node(1, Node(2, Node(3, Node(4, Node(5)))))
print(swap_every_two(node))
# 2, 1, 4, 3, 5