import heapq

def add(num, min_heap, max_heap):
  if len(min_heap) + len(max_heap) <= 1:
    heapq.heappush(max_heap, -num)
    return

  median = get_median(min_heap, max_heap)
  if num > median:
    heapq.heappush(min_heap, num)
  else:
    heapq.heappush(max_heap, -num)

def rebalance(min_heap, max_heap):
  if len(min_heap) > len(max_heap) + 1:
    root = heapq.heappop(min_heap)
    heapq.heappush(max_heap, -root)
  elif len(max_heap) > len(min_heap) + 1:
    root = -heapq.heappop(max_heap)
    heapq.heappush(min_heap, root)

def print_median(min_heap, max_heap):
  print(get_median(min_heap, max_heap))


def get_median(min_heap, max_heap):
  if len(min_heap) > len(max_heap):
    return min_heap[0]
  elif len(min_heap) < len(max_heap):
    return -max_heap[0]
  else:
    return (min_heap[0] + -max_heap[0]) / 2.0


def running_median(stream):
  min_heap = []
  max_heap = []
  answer = []
  for num in stream:
    add(num, min_heap, max_heap)
    rebalance(min_heap, max_heap)
    answer.append(get_median(min_heap, max_heap))
  return answer

def running_median2(stream):
    heapl, heapr = [], []
    res = []
    for num in stream:
        heapq.heappush(heapl, num)
        if len(heapl)-len(heapr) > 1:
            heapq.heappush(heapr, -(heapq.heappop(heapl)))
        if len(heapl) > len(heapr):
            res.append(heapl[0])
        else:
            res.append((heapl[0]-heapr[0])/2)
    return res

print(running_median([2, 1, 4, 7, 2, 0, 5]))
# [2, 1.5, 2, 3, 2, 2, 2]

print(running_median2([2, 1, 4, 7, 2, 0, 5]))
# [2, 1.5, 2, 3, 2, 2, 2]