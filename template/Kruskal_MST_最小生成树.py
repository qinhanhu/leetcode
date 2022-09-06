"""
将所有边按照权重从小到大排序，从权重最小的边开始遍历，如果这条边和mst中的其它边不会形成环，
则这条边是最小生成树的一部分，将它加入mst集合；否则，这条边不是最小生成树的一部分，
不要把它加入mst.
"""

# https://leetcode.cn/problems/min-cost-to-connect-all-points/
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