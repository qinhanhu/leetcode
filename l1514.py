import heapq
class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        # build graph
        graph = [{} for _ in range(n)]
        i = 0
        for u, v in edges:
            graph[u][v] = succProb[i]
            graph[v][u] = succProb[i]
            i += 1

        visited = set()
        maxheap = []
        probFromStart = [0] * n
        probFromStart[start] = 1
        heapq.heappush(maxheap, (-1, start))
        
        while maxheap:
            cur = heapq.heappop(maxheap)
            curProb = -cur[0]
            curNode = cur[1]
            visited.add(curNode)
            if curNode == end:
                break
            if curProb < probFromStart[curNode]:
                continue
            for neighbor, prob in graph[curNode].items():
                if neighbor not in visited:
                    nextProb = prob * curProb
                    if nextProb > probFromStart[neighbor]:
                        probFromStart[neighbor] = nextProb
                        heapq.heappush(maxheap, (-nextProb, neighbor))
        return probFromStart[end]
            
        