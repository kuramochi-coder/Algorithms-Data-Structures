# Most Frequent Subtree Sum
# Given the root of a binary tree, return the most frequent subtree sum. If there is a tie, return all the values with the highest frequency in any order.
# The subtree sum of a node is defined as the sum of all the node values formed by the subtree rooted at that node (including the node itself).

from collections import defaultdict

class Node():
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right


def _build_frequencies(root, counter):
    if root == None:
        return 0
    total = root.val + \
        _build_frequencies(root.left, counter) + \
        _build_frequencies(root.right, counter)
    counter[total] += 1
    return total


def most_freq_subtree_sum(root):
    counter = defaultdict(int)
    _build_frequencies(root, counter)
   
    max_frequency = max(counter.values())
    return [key for key, val in counter.items() if val == max_frequency]


root = Node(3, Node(1), Node(-3))
print(most_freq_subtree_sum(root))
# 1