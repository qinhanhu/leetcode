class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        edgesWithWeight = []
        n = len(points)
        for i in range(n):
            xi = points[i][0]
            yi = points[i][1]
            for j in range(i+1, n):
                xj = points[j][0]
                yj = points[j][1]
                weight = abs(xi - xj) + abs(yi - yj)
                edgesWithWeight.append((i, j, weight))
        edgesWithWeight.sort(key=lambda x: x[2])
        DS = DisjointSet(n)
        cost = 0
        for p1, p2, weight in edgesWithWeight:
            if DS.connected(p1, p2):
                continue
            DS.union(p1, p2)
            cost += weight
        
        return cost
            

class DisjointSet:
    def __init__(self, n):
        self.n = n
        self.parent = [i for i in range(n)]
        self.count = n
    
    def find(self, u):
        if self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u])
        return self.parent[u]

    def union(self, u, v):
        rootU = self.find(u)
        rootV = self.find(v)
        if rootU == rootV:
            return 
        self.parent[rootV] = rootU
        self.count -= 1
    
    def connected(self, u, v):
        return self.find(u) == self.find(v)

        