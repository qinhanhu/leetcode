import heapq
class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        rows, cols = len(heights), len(heights[0])
        effortFromStart = []
        for _ in range(rows):
            effortFromStart.append([float('inf')] * cols)
        effortFromStart[0][0] = 0
        minheap = []
        heapq.heappush(minheap, (0, 0, 0))
        # visited = set()
        while len(minheap) > 0:
            eff, x, y = heapq.heappop(minheap)
            # visited.add((x, y))
            if eff > effortFromStart[x][y]:
                continue
            for nextx, nexty in [(x-1, y), (x, y+1), (x+1, y), (x, y-1)]:
                # if 0 <= nextx <= rows - 1 and 0 <= nexty <= cols - 1 and (nextx, nexty) not in visited:
                if 0 <= nextx <= rows - 1 and 0 <= nexty <= cols - 1:
                    nextEff = max(effortFromStart[x][y], abs(heights[x][y] - heights[nextx][nexty]))
                    if nextEff < effortFromStart[nextx][nexty]:
                        effortFromStart[nextx][nexty] = nextEff
                        heapq.heappush(minheap, (nextEff, nextx, nexty))
        return effortFromStart[-1][-1]
            


        