
class Node(object):
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def count_unival_subtrees(node):
    count, is_unival = count_unival_subtrees_helper(node)
    return count, is_unival

# total_count, is_unival
def count_unival_subtrees_helper(node):
    if not node:
        return 0, True

    left_count, is_left_unival = count_unival_subtrees_helper(node.left)
    right_count, is_right_unival = count_unival_subtrees_helper(node.right)

    if (is_left_unival and is_right_unival and
            (not node.left or node.val == node.left.val) and
            (not node.right or node.val == node.right.val)):
        return left_count + right_count + 1, True

    return left_count + right_count, False


#    0
#   / \
#  1   0
#     / \
#    1   0
#   / \
#  1   1
a = Node(0)
a.left = Node(1)
a.right = Node(0)
a.right.left = Node(1)
a.right.right = Node(0)
a.right.left.left = Node(1)
a.right.left.right = Node(1)

print(count_unival_subtrees(a))
# 5