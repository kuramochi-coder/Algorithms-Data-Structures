
def merge(intervals):
    results = []
    for start, end in sorted(intervals, key=lambda x: x[0]):
        if results and start <= results[-1][1]:
            prev_start, prev_end = results[-1]
            results[-1] = (prev_start, max(prev_end, end))
        else:
            results.append((start, end))

    return results


print(merge(([1, 3], [5, 8], [4, 10], [20, 25])))
# [(1, 3), (4, 10), (20, 25)]