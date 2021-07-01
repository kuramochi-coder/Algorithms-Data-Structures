
import heapq
import collections

class Solution(object):
    # time complexity: O(nlogn), space complexity: O(n)
    def topKFrequentNonHeap(self, nums, k):
        count = {}
        for num in nums:
            count[num] = count.get(num, 0) + 1

        count_array = list(count.items())
        count_array.sort(key=lambda x: x[1])
        # count array is [(3, 1), (2, 2), (1, 3)], arranged in (number, count) format in the array

        result = []
        for i in range(k):
            result.append(count_array.pop()[0]) #index 0 here because that is the number, it will pop the highest count
        
        return result

    # time complexity: O(klogn), space complexity: O(n)
    def topKFrequent(self, nums, k):
        count = collections.defaultdict(int)
        for n in nums:
            count[n] += 1

        heap = []
        for num, c in count.items():
            heap.append((-c, num)) #python sorts the heap using the first item, default in python is min heap
        heapq.heapify(heap)
        # heap is [(-3, 1), (-2, 2), (-1, 3)], arranged in (count, number) format

        result = []
        for i in range(k):
            result.append(heapq.heappop(heap)[1]) #index 1 here because that is the number
        return result

print(Solution().topKFrequentNonHeap([1, 1, 1, 2, 2, 3, ], 2))
# [1, 2]

print(Solution().topKFrequent([1, 1, 1, 2, 2, 3, ], 2))
# [1, 2]