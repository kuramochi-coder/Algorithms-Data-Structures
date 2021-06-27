class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next

class Linked_List:
    def __init__(self):  
        self.head = None

    def append(self, val):
        if self.head is None:
            self.head = Node(val)
            return

        self._append(val, self.head)

    def _append(self, val, current):
        if current.next is None:
            current.next = Node(val)
            return
        
        self._append(val, current.next)

    def print(self, head):
        output = self._print(head)
        return print(output)

    
    def _print(self, current):
        if current is None:
            return ''
        
        return current.val + '->' + self._print(current.next)

    def contains(self, target):
        return self._contains(target, self.head)

    def _contains(self, target, current):
        if current is None:
            return False
        
        if target == current.val:
            return True

        return self._contains(target, current.next)

# time complexity: O(n), space complexity: O(1)
def sum_list_iterative(head):
    total_sum = 0
    current = head

    while current is not None:
        total_sum += current.val
        current = current.next
    
    return total_sum

# time complexity: O(n), space complexity: O(n)
def sum_list_recursive(head):
    if head is None:
        return 0
    
    return head.val + sum_list_recursive(head.next)

# time complexity: O(n), space complexity: O(1) because the deletion is in-place
def delete_value_iterative(head, target):
    if head.val == target:
        return head.next
    
    previous = None
    current = head

    while current is not None:
        if current.val == target:
            previous.next = current.next

        previous = current
        current = current.next
    
    return head

# time complexity: O(n), space complexity: O(n) because we have to use n-stack frames in call stack
def delete_value_recursive(head, target):
    if head.val == target:
        return head.next

    _delete_value_recursive(head, None, target)
    return head

def _delete_value_recursive(current, previous, target):
    if current is None:
        return
    
    if current.val == target:
        previous.next = current.next
        return
    
    return _delete_value_recursive(current.next, current, target)

# time complexity: O(n), space complexity: O(1) because the modification is in-place
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



# create linked list with nodes
list = Linked_List()

# list.append(11)
# list.append(7)
# list.append(10)
# list.append(2)

# print(sum_list_iterative(list.head))
# print(sum_list_recursive(list.head))

list.append('a')
list.append('b')
list.append('c')
list.append('d')
list.append('e')

# list.print(list.head)

# print(list.contains('a')) #True 
# print(list.contains('b')) #True
# print(list.contains('c')) #True
# print(list.contains('d')) #True
# print(list.contains('e')) #True
# print(list.contains('z')) #False

list.print(list.head)
print('#####################')

# new_head = delete_value_iterative(list.head, 'a')
# new_head = delete_value_recursive(list.head, 'e')

# new_head = reverse_list_iterative(list.head)
new_head = reverse_list_recursive(list.head)

list.print(new_head)