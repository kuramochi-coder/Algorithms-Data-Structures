# Intersection of Two Linked Lists
# Given the heads of two singly linked-lists headA and headB, 
# return the node at which the two lists intersect. If the two linked lists have no intersection at all, return null.

class Node(object):
  def __init__(self, value, next=None):
    self.value = value
    self.next = next

class Solution(object):
    # brute force solution
    def getIntersectionNode(self, a, b):
        hash_set = set()
        
        while not a is None:
            hash_set.add(a)
            a = a.next
            
        while not b is None:
            if b in hash_set:
                return b
            
            b = b.next
            
        return None

# Optimal solution by coder pro below
    def _length(self, n):
        len = 0
        curr = n
        while curr:
            curr = curr.next
            len += 1
        return len

    def intersection(self, a, b):
        lenA = self._length(a)
        lenB = self._length(b)
        currA = a
        currB = b

        if lenA > lenB:
            for _ in range(lenA - lenB):
                currA = currA.next
        else:
            for _ in range(lenB - lenA):
                currB = currB.next

        while currA != currB:
            currA = currA.next
            currB = currB.next

        return currA

a = Node(1)
a.next = Node(2)
a.next.next = Node(3)
a.next.next.next = Node(4)

b = Node(6)
b.next = a.next.next

print(Solution().getIntersectionNode(a, b).value)
# 3

print(Solution().intersection(a, b).value)
# 3