class Solution:
    def __init__(self):
        self.n = 1000
        self.father = [i for i in range(0, self.n+1)]
        # print(self.father)

    def find(self, u:int):
        # print(u)
        if u == self.father[u]:
            return u
        self.father[u] = self.find(self.father[u])
        return self.father[u]
    
    def join(self, u, v:int):
        u = self.find(u)
        v = self.find(v)
        if u == v:
            return
        self.father[v] = u
    
    def same(self, u, v: int):
        return self.find(u) == self.find(v)


    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:

        for e in edges:
            if self.same(e[0], e[1]):
                return e
            else:
                self.join(e[0], e[1])
        

    