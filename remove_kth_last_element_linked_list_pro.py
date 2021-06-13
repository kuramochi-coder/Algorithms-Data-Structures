# Remove k-th Last Element From Linked List
# You are given a singly linked list and an integer k. Return the linked list, removing the k-th last element from the list. 
# Try to do it in a single pass and using constant space.

class Node:
    def __init__(self, val, next):
        self.val = val
        self.next = next

    def __str__(self):
        n = self
        answer = ''
        while n:
            answer += str(n.val)
            n = n.next
        return answer

def remove_kth_from_linked_list(node, k):
    slow, fast = node, node
    for i in range(k):
        fast = fast.next
    if not fast:
        return node.next

    prev = None
    while fast:
        prev = slow
        fast = fast.next
        slow = slow.next
    prev.next = slow.next
    return node

def remove_kth_from_linked_list2(node, k):
    slow, fast = node, node

    for i in range(k):
        fast = fast.next
    
    while fast.next:
        slow = slow.next
        fast = fast.next
    
    slow.next = slow.next.next
    return node

head = Node(1, Node(2, Node(3, Node(4, Node(5, None)))))
head2 = Node(1, Node(2, Node(3, Node(4, Node(5, None)))))
print(head)
# 12345
result = remove_kth_from_linked_list(head, 1)
print(result)
# 1234
print('---')
print(head2)
result2 = remove_kth_from_linked_list2(head2, 1)
print(result2)
# 1234