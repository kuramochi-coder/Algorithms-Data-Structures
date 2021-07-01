# Remove Duplicates from Sorted List
# Given the head of a sorted linked list, 
# delete all duplicates such that each element appears only once. Return the linked list sorted as well.
# Input: head = [1,1,2]
# Output: [1,2]

class Node(object):
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def __repr__(self):
        n = self
        ret = ''
        while n:
            ret += str(n.value) + ' '
            n = n.next
        return ret


def remove_duplicates(node):
    curr = node

    while curr and curr.next:
        if curr.value == curr.next.value:
            curr.next = curr.next.next
        else:
            curr = curr.next

def remove_duplicates2(node):
    seen = set()

    prev = Node(None)
    head = curr = node

    while curr:
        if curr.value in seen:
            prev.next = curr.next
        else:
            seen.add(curr.value)
            prev = curr
            
        curr = curr.next
         

    return head



node = Node(1, Node(2, Node(2, Node(3, Node(3)))))
node2 = Node(1, Node(2, Node(2, Node(3, Node(3)))))
remove_duplicates(node)
print(node)
# (1, (2, (3, None)))
print(remove_duplicates2(node2))
