class DisjointSet:
    def __init__(self, n):
        self.n = n
        self.groupCnt = n
        self.parent = [i for i in range(n)]
        # self.groups = {}
        # for i in range(n):
        #     self.groups[i] = set([i])

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
        self.groupCnt -= 1
        # self.groups[rootU].update(self.groups[rootV])
        # del self.groups[rootV]
        

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        emailToAcc = {}
        accToEmail = {}
        n = len(accounts)
        DS = DisjointSet(n)

        for i in range(n):
            accToEmail[i] = []
            for j in range(len(accounts[i])):
                if j > 0:
                    if accounts[i][j] not in emailToAcc:
                        emailToAcc[accounts[i][j]] = i
                    else:
                        DS.union(i, emailToAcc[accounts[i][j]])
                    accToEmail[i].append(accounts[i][j])
        
        # res = []
        # for _, indexSet in DS.groups.items():
        #     indexList = list(indexSet)
        #     name = accounts[indexList[0]][0]
        #     res.append([name])
        #     emails = set()
        #     for i in indexList:
        #         emails.update(accToEmail[i])
        #     res[-1] += sorted(list(emails))
        # return res

        indexToEmail = {}
        for i in range(n):
            parent = DS.find(i)
            if parent not in indexToEmail:
                indexToEmail[parent] = set()
            indexToEmail[parent].update(accToEmail[i])
        
        res = []
        for index, emails in indexToEmail.items():
            name = accounts[index][0]
            res.append([name])
            res[-1] += sorted(list(emails))
        return res


        
        
                        

        