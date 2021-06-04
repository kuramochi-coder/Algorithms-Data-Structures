# Number of Provinces
# There are n cities. Some of them are connected, while some are not. 
# If city a is connected directly with city b, and city b is connected directly with city c, then city a is connected indirectly with city c.
# A province is a group of directly or indirectly connected cities and no other cities outside of the group.
# You are given an n x n matrix isConnected where isConnected[i][j] = 1 if the ith city and the jth city are directly connected, and isConnected[i][j] = 0 otherwise.
# Return the total number of provinces.

class Solution:
    # dfs solution
    def findCircleNum(self, isConnected):
        visited = set()
        province_count = 0
        
        for start in range(len(isConnected)):
            if start not in visited:
                province_count += 1
                self.dfs(start, visited, isConnected)
        
        return province_count
        
                    
    def dfs(self, city, visited, isConnected):
        visited.add(city)
        
        # note that this is a nxn matrix, so end does not have to be in range of len(isConnected[city])
        for end in range(len(isConnected)):
            if isConnected[city][end] == 1 and end not in visited:
                self.dfs(end, visited, isConnected)

class Solution2:
    # union find solution
    def findCircleNum2(self, isConnected):
        
        id = list(range(len(isConnected)))
        size = [1] * len(isConnected)
        
        def root(x):
            while id[x] != x:
                id[x] = id[id[x]] # path compression
                x = id[x]
            return x
        
        def union(x, y):
            root_x = root(x)
            root_y = root(y)
            if size[root_x] < size[root_y]: 
                smaller, bigger = root_x, root_y
            else:
                smaller, bigger = root_y, root_x
            id[smaller] = bigger 
            size[bigger] += size[smaller]
        
        for i in range(len(isConnected)):
            for j in range(i+1):
                if i!=j and isConnected[i][j] == 1:
                    union(i, j)
        
        count = 0
        for i, j in enumerate(id):
            if i == j:
                count += 1
        return count

print(Solution().findCircleNum([[1,1,0],[1,1,0],[0,0,1]]))
# 2
print(Solution().findCircleNum([[1,0,0],[0,1,0],[0,0,1]]))
# 3