
class Solution:
    def intersection(self, nums1, nums2):
        results = {}
        for num in nums1:
            if num in nums2 and num not in results:
                results[num] = 1
        return list(results.keys())

    def intersection2(self, nums1, nums2):
        set1 = set(nums1)
        set2 = set(nums2)
        return [x for x in set1 if x in set2]

    def intersection3(self, nums1, nums2):
        hash = {}
        # duplicates = {}
        duplicates = set()
        for num in nums1:
            hash[num] = 1
        for num in nums2:
            if num in hash:
                # duplicates[num] = 1
                duplicates.add(num)

        # return tuple(duplicates.keys())
        return tuple(duplicates)

print(Solution().intersection([4, 9, 5], [9, 4, 9, 8, 4]))
# (9, 4)

print(Solution().intersection2([4, 9, 5], [9, 4, 9, 8, 4]))
# (9, 4)

print(Solution().intersection3([4, 9, 5], [9, 4, 9, 8, 4]))
# (9, 4)