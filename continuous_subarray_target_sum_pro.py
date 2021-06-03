
def find_continuous_k(list, k):
    for start in range(len(list)):
        sum = 0
        for end in range(start, len(list)):
            sum += list[end]
            if sum == k:
                return list[start:end + 1]
    return None


def find_continuous_k_2(list, k):
  previous_sums = {0: -1}
  sum = 0
  for index, n in enumerate(list):
    sum += n
    previous_sums[sum] = index
    if previous_sums.get(sum - k):
      return list[previous_sums[sum-k] + 1: index + 1]
  return None


print(find_continuous_k([1, 3, 2, 5, 7, 2], 14))
print('---')
print(find_continuous_k_2([1, 3, 2, 5, 7, 2], 14))
# [2, 5, 7]