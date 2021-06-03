""" 
n: length of array
time complexity is O(2^n) and space complexity is O(n^2)
"""

def combinations(elements):
    if len(elements) == 0:
        return [[]]

    first_element = elements[0]
    rest_of_elements = elements[1:]

    combinations_without_first = combinations(rest_of_elements)
    combinations_with_first = []

    final_combinations = []

    # comb_with_first = [[first_element] + combination for combination in combinations_without_first]
    # combinations_with_first.extend(comb_with_first)
    for comb in combinations_without_first:
        comb_with_first = [*comb, first_element] #similar to spread operator in javascript [...comb, first_element]
        combinations_with_first.append(comb_with_first)

    final_combinations.extend(combinations_with_first)
    final_combinations.extend(combinations_without_first)

    return final_combinations

print(combinations(['a', 'b', 'c']))
print('###############################')
print(combinations(['b', 'c']))