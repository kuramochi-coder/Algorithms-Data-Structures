
class Node(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        c = self
        answer = ''
        while c:
            answer += str(c.val) + ' ' if c.val else ""
            c = c.next
        return answer


def merge(lists):
    arr = []
    for node in lists:
        while node:
            arr.append(node.val)
            node = node.next
    head = root = None
    for val in sorted(arr):
        if not root:
            head = root = Node(val)
        else:
            root.next = Node(val)
            root = root.next
    return head


def merge2(lists):
    head = current = Node(-1)

    while any(list is not None for list in lists):
        current_min, i = min((list.val, i)
                            for i, list in enumerate(lists) if list is not None)
        # here i is index 0 or 1, where lists[0] is a and lists[1] is b
        # print(current_min, i)
        lists[i] = lists[i].next
        current.next = Node(current_min)
        current = current.next

    return head.next

# this is my solution
def merge3(lists):
    a_list = lists[0]
    b_list = lists[1]

    result = Node(0)
    dummy = result

    while a_list and b_list:
        if a_list.val < b_list.val:
            result.next = Node(a_list.val)
            result = result.next
            a_list = a_list.next
        else:
            result.next = Node(b_list.val)
            result = result.next
            b_list = b_list.next

    while a_list:
        result.next = Node(a_list.val)
        result = result.next
        a_list = a_list.next 

    while b_list:
        result.next = Node(b_list.val)
        result = result.next
        b_list = b_list.next 

    return dummy.next



a = Node(1, Node(3, Node(5)))
b = Node(2, Node(4, Node(6)))

print(a)
# 135
print(b)
# 246
print(merge([a, b]))
print(merge2([a, b]))
print(merge3([a, b]))
# 123456