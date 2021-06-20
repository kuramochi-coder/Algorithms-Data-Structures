def find_fixed_point_helper(low, high, nums):
    if low == high:
        return None

    mid = int((low + high) / 2)
    if nums[mid] == mid:
        return mid
    if nums[mid] < mid:
        return find_fixed_point_helper(mid+1, high, nums)
    else:
        return find_fixed_point_helper(low, mid, nums)


def find_fixed_point(nums):
    return find_fixed_point_helper(0, len(nums), nums)


def find_fixed_point_iterative(nums):
    low = 0
    high = len(nums)

    while (low != high):
        mid = int((low + high) / 2)
        if nums[mid] == mid:
            return mid
        if nums[mid] < mid:
            low = mid + 1
        else:
            high = mid

    return None


print(find_fixed_point([-5, 1, 3, 4]))
# 1

print(find_fixed_point_iterative([-5, 1, 3, 4]))
# 1