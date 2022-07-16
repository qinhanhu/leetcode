class Solution:
    def __init__(self):
        self.n = 1000
        self.father = [i for i in range(0, self.n+1)]
    
    def initFather(self):
        self.father = [i for i in range(0, self.n+1)]
    
    def find(self, u):
        if u == self.father[u]:
            return u
        self.father[u] = self.find(self.father[u])
        return self.father[u]
    
    def join(self, u, v):
        u = self.find(u)
        v = self.find(v)
        if u == v:
            return
        self.father[v] = u
    
    def same(self, u, v):
        return self.find(u) == self.find(v)

    def getRemovedEdge(self, edges):
        for e in edges:
            if self.same(e[0], e[1]):
                return e
            else:
                self.join(e[0], e[1])
        return []

    def isTreeAfterRemovedEdge(self, edges, edge):
        self.initFather()
        for e in edges:
            if e == edge:
                continue
            if self.same(e[0], e[1]):
                return False
            else:
                self.join(e[0], e[1])
        return True


    def findRedundantDirectedConnection(self, edges: List[List[int]]) -> List[int]:
        inDrgree = {}
        edgesWithTwoInDegree = []
        for e in edges:
            if e[1] not in inDrgree:
                inDrgree[e[1]] = 1
            else:
                inDrgree[e[1]] += 1
        for e in edges:
            if inDrgree[e[1]] == 2:
                edgesWithTwoInDegree.append(e)
        # print(edgesWithTwoInDegree)
        if len(edgesWithTwoInDegree) == 2:
            for i in range(1, -1, -1):
                if self.isTreeAfterRemovedEdge(edges, edgesWithTwoInDegree[i]):
                    return edgesWithTwoInDegree[i]
        else:
            return self.getRemovedEdge(edges)


