# Unique Binary Search Trees
# Given an integer n, 
# return the number of structurally unique BST's (binary search trees) which has exactly n nodes of unique values from 1 to n.
# Input: n = 3
# Output: 5

class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def __repr__(self):
        result = str(self.value)
        if self.left:
            result = result + str(self.left)
        if self.right:
            result = result + str(self.right)
        return result

class Solution:
    def gen_tree(self, nums):
        if len(nums) == 0:
            return [None]
        if len(nums) == 1:
            return [Node(nums[0])]

        bsts = []

        for n in nums:
            lefts = self.gen_tree(range(nums[0], n))
            rights = self.gen_tree(range(n + 1, nums[-1] + 1))

            for left in lefts:
                for right in rights:
                    tree = Node(n, left, right)
                    bsts.append(tree)

        return bsts


    def generate_bst(self, n):
        return self.gen_tree(range(1, n + 1))

class Solution2:
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n==0 or n==1:
            return 1
        
        dp = [0]*(n+1)
        dp[0] = 1
        dp[1] = 1
        
        
        for i in range(2, n+1):
            for j in range(i):
                dp[i]+=dp[i-j-1] * dp[j]
                
        return dp[n]

print(Solution().generate_bst(3))
# 5 trees
print(Solution2().numTrees(3))
# 5 trees