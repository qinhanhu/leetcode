import heapq
class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        """
        input: grid is list[list[int]], grid[i][j] >= 0
        output: int, the least time needed to reach (n-1,n-1) from (0,0)
        
        idea:
        Similar to Dijkstra Algo, 
        1. we start BFS from (0,0) and use Priority Queue(minHeap) to update nodes that can be reached,
        2. every step we chose the node with the lowest elevation from candidate nodes.
        3. record and update the max elevation on the nodes we passed.

        Time: O(n^2logn)
        Space: O(n^2) size of minHeap
        """
        # time needed to reach (i, j) ffrom start
        n = len(grid)
        timeFromStart = []
        for i in range(n):
            timeFromStart.append([n*n] * n)
        timeFromStart[0][0] = 0
        minHeap = []
        # heap[(value, (x,y))]
        heapq.heappush(minHeap, (grid[0][0], (0,0)))
        res = -1
        while len(minHeap) > 0:
            cur = heapq.heappop(minHeap)
            val = cur[0]
            node = cur[1]
            i, j = node[0], node[1]
            res = max(res, val)
            if i == n-1 and j == n-1:
                break
            for nexti, nextj in [(i,j+1), (i,j-1), (i+1, j), (i-1, j)]:
                if 0<=nexti<=n-1 and 0<=nextj<=n-1 and grid[nexti][nextj] < timeFromStart[nexti][nextj]:
                    timeFromStart[nexti][nextj] = grid[nexti][nextj]
                    heapq.heappush(minHeap, (grid[nexti][nextj], (nexti, nextj)))
        return res