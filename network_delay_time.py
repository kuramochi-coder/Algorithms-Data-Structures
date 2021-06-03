# You are given a network of n nodes, labeled from 1 to n. 
# You are also given times, a list of travel times as directed edges times[i] = (ui, vi, wi), 
# where ui is the source node, vi is the target node, and wi is the time it takes for a signal to travel from source to target.
# We will send a signal from a given node k. 
# Return the time it takes for all the n nodes to receive the signal. 
# If it is impossible for all the n nodes to receive the signal, return -1.

import heapq

# This solution uses Dijkstra's Shortest Path implemented with a binary min heap. 
# Time Complexity: O(|E|log|E|), where |E| is the number of edges in the graph G = (V, E).
class Solution:
    def networkDelayTime(self, times, n, k): # n is total number of nodes, k is the starting node
        # times[i] = (ui, vi, wi), where ui is the source node, vi is the target node, 
        # and wi is the time it takes for a signal to travel from source to target.
        graph = {}  # create graph
        for u, v, w in times:
            if u not in graph.keys():
                graph[u] = [(v, w)]
            else:
                graph[u].append((v, w))

        min_heap = [(0, k)] # push starting node k into heap, cost is 0
        visited_n_costs = {}

        while len(min_heap) > 0:
            cost, node = heapq.heappop(min_heap)    # pop node with smallest cost
            if node in visited_n_costs.keys():    # check for duplicates
                continue
            visited_n_costs[node] = cost
            if node not in graph.keys():    # prevent key error
                continue
            for neighbor, c in graph[node]:
                if neighbor not in visited_n_costs.keys():
                    heapq.heappush(min_heap, (cost + c, neighbor)) # push all the neighbors into heap (may push duplicate nodes)
        
        if len(visited_n_costs) == n:
            return max(visited_n_costs.values())
        else:
            return -1

# times[i] = (ui, vi, wi), where ui is the source node, vi is the target node, 
# and wi is the time it takes for a signal to travel from source to target.
print(Solution().networkDelayTime([[2,1,1],[2,3,1],[3,4,1]], 4, 2))
# 2
print('---')
print(Solution().networkDelayTime([[1,2,1]], 2, 1))
# 1
print('---')
print(Solution().networkDelayTime([[1,2,1]], 2, 2))
# -1