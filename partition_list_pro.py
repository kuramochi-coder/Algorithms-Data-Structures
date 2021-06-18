def partition(nums, k):
    low = 0
    high = len(nums) - 1

    i = 0
    while i <= high:
        n = nums[i]
        if n > k:
            nums[high], nums[i] = nums[i], nums[high]
            high -= 1
        if n < k:
            nums[low], nums[i] = nums[i], nums[low]
            low += 1
            i += 1
        if n == k:
            i += 1

    return nums


def partitionSort(nums, k):
    return sorted(nums)


def partitionCopy(nums, k):
    a = []
    b = []
    for n in nums:
        if n < k:
            a.append(n)
        else:
            b.append(n)
    return a + b


print(partition([8, 9, 9, 2, 4, 1, 1, 0], 3))