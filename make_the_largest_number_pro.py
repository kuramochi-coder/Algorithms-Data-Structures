# Largest Number
# Given a list of non-negative integers nums, arrange them such that they form the largest number.
# Note: The result may be very large, so you need to return a string instead of an integer.

from functools import cmp_to_key

def largestNum(nums):
    sorted_nums = sorted(nums, key=cmp_to_key(
        lambda a, b:
        1 if str(a) + str(b) < str(b) + str(a) # put in front in a+b combination is greater
        else -1)
    )
    return ''.join(str(n) for n in sorted_nums)

def largestNumber(nums):
        sorted_nums = sorted(nums, key=cmp_to_key(
            lambda a, b:
            -1 if str(a) + str(b) > str(b) + str(a) else 1 # put in front in a+b combination is greater 
        ))

        # return str(int("".join(map(str, sorted_nums)))) # this is faster than the return method below 
        return str(int(''.join(str(n) for n in sorted_nums))) # this way of returning prevents errors like [0, 0] combinations

print(largestNum([17, 7, 2, 45, 72]))
# 77245217
print('---')
print(largestNumber([17, 7, 2, 45, 72]))
# 77245217