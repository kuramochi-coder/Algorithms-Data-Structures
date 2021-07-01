
class Solution:
    def findPythagoreanTriplets(self, nums):
        for a in nums:
            for b in nums:
                for c in nums:
                    if a*a + b*b == c*c:
                        return True
        return False

    # time complexity: O(n^2), space complexity: O(n) because a set is created
    def findPythagoreanTriplets2(self, nums):
        squares = set([n*n for n in nums])

        for a in nums:
            for b in nums:
                if a * a + b * b in squares:
                    return True
        return False

print(Solution().findPythagoreanTriplets2([3, 5, 12, 5, 13]))
# True