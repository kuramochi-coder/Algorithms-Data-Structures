
class Solution:
    def searchRange(self, nums, target):
        # first_occurence_index = self.binary_search_recursive(nums, 0, len(nums) - 1, target, True)
        # last_occurence_index = self.binary_search_recursive(nums, 0, len(nums) - 1, target, False)

        first_occurence_index = self.binary_search_iteratve(nums, 0, len(nums) - 1, target, True)
        last_occurence_index = self.binary_search_iteratve(nums, 0, len(nums) - 1, target, False)

        return [first_occurence_index, last_occurence_index]
    
    def binary_search_recursive(self, nums, left, right, target, find_first):
        if left > right:
            return -1   # return -1 instead of False here because question wants index
        
        mid = (left + right) // 2

        if find_first:
            if (mid == 0 or target > nums[mid - 1]) and nums[mid] == target:
                return mid
            elif target > nums[mid]:
                return self.binary_search_recursive(nums, mid + 1, right, target, find_first)
            else:
                return self.binary_search_recursive(nums, left, mid - 1, target, find_first)
        else:
            if (mid == len(nums) - 1 or target < nums[mid + 1]) and nums[mid] == target:
                return mid
            elif target < nums[mid]:
                return self.binary_search_recursive(nums, left, mid - 1, target, find_first)
            else:
                return self.binary_search_recursive(nums, mid + 1, right, target, find_first)

    def binary_search_iteratve(self, nums, left, right, target, find_first):
        while left <= right:
            if left > right:
                return -1   # return -1 instead of False here because question wants index
            
            mid = (left + right) // 2

            if find_first:
                if (mid == 0 or target > nums[mid - 1]) and nums[mid] == target:
                    return mid
                elif target > nums[mid]:
                    left = mid + 1
                else:
                    right = mid - 1
            else:
                if (mid == len(nums) - 1 or target < nums[mid + 1]) and nums[mid] == target:
                    return mid
                elif target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1

    # solutions below by coder pro
    def getRange(self, arr, target):
        first = self.binarySearchIterative(arr, 0, len(arr) - 1, target, True)
        last = self.binarySearchIterative(arr, 0, len(arr) - 1, target, False)
        return [first, last]

    def binarySearchRecursive(self, arr, low, high, target, findFirst):
        if high < low:
            return -1
        mid = low + (high - low) // 2
        if findFirst:
            if (mid == 0 or target > arr[mid - 1]) and arr[mid] == target:
                return mid
            if target > arr[mid]:
                return self.binarySearch(arr, mid + 1, high, target, findFirst)
            else:
                return self.binarySearch(arr, low, mid - 1, target, findFirst)
        else:
            if (mid == len(arr)-1 or target < arr[mid + 1]) and arr[mid] == target:
                return mid
            elif target < arr[mid]:
                return self.binarySearch(arr, low, mid - 1, target, findFirst)
            else:
                return self.binarySearch(arr, mid + 1, high, target, findFirst)

    def binarySearchIterative(self, arr, low, high, target, findFirst):
        while True:
            if high < low:
                return -1
            mid = low + (high - low) // 2
            if findFirst:
                if (mid == 0 or target > arr[mid - 1]) and arr[mid] == target:
                    return mid
                if target > arr[mid]:
                    low = mid + 1
                else:
                    high = mid - 1
            else:
                if (mid == len(arr)-1 or target < arr[mid + 1]) and arr[mid] == target:
                    return mid
                elif target < arr[mid]:
                    high = mid - 1
                else:
                    low = mid + 1


arr = [1, 3, 3, 5, 7, 8, 9, 9, 9, 15]
x = 9
print(Solution().getRange(arr, 9))
# [6, 8]
print(Solution().searchRange(arr, 9))