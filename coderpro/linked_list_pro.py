class Node(object):
  def __init__(self, value, next=None):
    self.value = value
    self.next = next
  
  def __str__(self):
    curr = self
    output = ''
    while curr:
      output += str(curr.value)
      curr = curr.next
    return output

def list2LinkedList(nums):
  head = None
  curr = None
  for n in nums:
    if not head:
      head = Node(n)
      curr = head
    else:
      curr.next = Node(n)
      curr = curr.next
  return head

def reverse_list_iterative(head):
    previous = None
    current = head

    while current is not None:
        # store original next pointer
        _next = current.next

        # reverse here
        current.next = previous

        previous = current
        current = _next
    
    return previous

def reverse_list_recursive(current, previous=None):
    if current is None:
        return previous

    _next = current.next
    current.next = previous

    return reverse_list_recursive(_next, current)

n = Node(1, Node(2, Node(3)))
print(n)

# print(list2LinkedList([10, 20, 30]))
head = list2LinkedList([10, 20, 30])
print(head)
# new_head = reverse_list_iterative(head)
new_head = reverse_list_recursive(head)
print(new_head)