class Solution:
    def shortestDistance(self, grid: List[List[int]]) -> int:
        """
        1. for every building, 
           get shortest travel distances between the building with every empty land.      (using BFS)
           
           i.e. we can get
                STDfromB1 = [m * n]
                STDfromB2 = [m * n]
                STDfromB3 = [m * n]
        2. Iterate empty land (i, j), 
           find min(STDfromB1[i,j] + STDfromB2[i,j] + STDfromB3[i,j])
        """
        # find bulidings
        m = len(grid)
        n = len(grid[0])
        buildings = []
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    buildings.append((i, j))
                
        STDs = []
        for start in buildings:
            STD, flag = self.bfs(grid, start)
            if not flag:
                return -1
            STDs.append(STD)
        _min = float('inf')
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    _sum = 0
                    for x in range(len(STDs)):
                        _sum += STDs[x][i][j]
                    _min = min(_min, _sum)
        return _min if _min != float('inf') else -1
            
    def bfs(self, graph, start):
        que = collections.deque()
        que.append(start)
        distance = 0
        m = len(graph)
        n = len(graph[0])
        STD = []
        for i in range(m):
            STD.append([float('inf')] * n)
        visited = set()
        visited.add(start)
        while len(que) > 0:
            size = len(que)
            for _ in range(size):
                i, j = que.popleft()
                STD[i][j] = distance
                for nexti, nextj in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]:
                    if 0 <= nexti <= m-1 and 0 <= nextj <= n-1 and (nexti,nextj) not in visited and graph[nexti][nextj] == 0:
                        que.append((nexti, nextj))
                        visited.add((nexti, nextj))
            distance += 1
        return STD, len(visited) > 1
            
                        
                
                
        
        
        