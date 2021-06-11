# Squares of a Sorted Array
# Given an integer array nums sorted in non-decreasing order, 
# return an array of the squares of each number sorted in non-decreasing order.
# Input: nums = [-7,-3,2,3,11]
# Output: [4,9,9,49,121] 

def square_numbers(nums):
    neg_i = -1
    i = 0

    result = []
    for n in nums:
        if n >= 0:
            if neg_i == -1:
                neg_i = i - 1

            while neg_i >= 0 and nums[neg_i] < 0 and -nums[neg_i] < nums[i]:
                val = nums[neg_i]
                result.append(val * val)
                neg_i -= 1

            val = nums[i]
            result.append(val * val)
        i += 1

    while neg_i >= 0 and nums[neg_i] < 0:
        val = nums[neg_i]
        result.append(val * val)
        neg_i -= 1

    return result

def square_numbers2(nums):
    result = []
        
    for num in nums:
        sq = num*num
        result.append(sq)
    
    result = sorted(result)
    
    return result


print(square_numbers([-5, -3, -1, 0, 1, 4, 5]))
print('---')
print(square_numbers2([-5, -3, -1, 0, 1, 4, 5]))