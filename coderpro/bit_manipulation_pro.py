def num2bits(num):
    result = ''
    while num:
        result = str(num & 1) + result
        num = num >> 1
    return result


def bits2num(bits):
    num = 0
    for bit in bits:
        num = num << 1
        if bit == '1':
            num += 1
    return num


def count_bits(num):
    num_bits = 0
    while num:
        num_bits += num & 1
        num >>= 1
    return num_bits


print(num2bits(5))
# 101

print(bits2num('101'))
# 5

print(num2bits(34))
# 100010

print(count_bits(34))
# 2

# Given an array [4, 1, 4, 2, 2] where all numbers appear twice except for one number.
# Find that number.

def singleNumber(nums):
    result = 0
    for n in nums:
        result ^= n
    return result


print(singleNumber([4, 1, 4, 2, 2]))
# 1