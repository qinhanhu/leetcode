# https://leetcode.cn/problems/network-delay-time/
import heapq
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:    

        minHeap = []
        graph = []
        for _ in range(n):
            graph.append({})
        
        for u, v, w in times:
            graph[u-1][v-1] = w
            
        
        disFromStart = [float('inf')] * n
        disFromStart[k-1] = 0
        heapq.heappush(minHeap, (0, k-1))
        while len(minHeap) > 0:
            curDisFromStart, cur = heapq.heappop(minHeap)
            if curDisFromStart > disFromStart[cur]:
                continue
            for neighbor, weight in graph[cur].items():
                if curDisFromStart + weight < disFromStart[neighbor]:
                    disFromStart[neighbor] = curDisFromStart + weight
                    heapq.heappush(minHeap, (curDisFromStart + weight, neighbor))
        res = max(disFromStart)
        if res == float('inf'):
            return -1
        else:
            return res

def dijkstra(start, graph):
    """
    Time: O(V + ElogV)
    """
        
    # 维护start到各个点的最短路径权重
    disFromStart = [float('inf')] * n
    disFromStart[start] = 0
    # 记录每个节点的父节点，后续可以DFS输出路径
    parents = [i for i in range(n)]


    minHeap = [] # heap 按距离(权重)排序
    # 从start开始BFS 
    heapq.heappush(minHeap, (0, start))
    while len(minHeap) > 0:
        curDisFromStart, cur = heapq.heappop(minHeap)
        if curDisFromStart > disFromStart[cur]:
            continue
        # 将cur的相邻节点装入heap
        for neighbor, disToNeighbor in graph[cur].items():
            if curDisFromStart + disToNeighbor < disFromStart[neighbor]:
                disFromStart[neighbor] = curDisFromStart + disToNeighbor
                heapq.heappush(minHeap, (curDisFromStart + disToNeighbor, neighbor))
                parents[neighbor] = cur

    return disFromStart

def getPath(start, end, parents):
    path = []
    cur = end
    while True:
        path.append(cur)
        if cur == start:
            break
        cur = parents[cur]
    return path[::-1]

            

