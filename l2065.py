#L2065: https://leetcode.cn/problems/maximum-path-quality-of-a-graph/
class Solution:
    def __init__(self):
        self.res = 0

    def maximalPathQuality(self, values: List[int], edges: List[List[int]], maxTime: int) -> int:
        """
        Since There are at most four edges connected to each node 
        and 10 <= timej, maxTime <= 100 that means len(path) <= 10.
        if we iterate every path, the time complexity is O(4 ** 10)
        so we could use dfs + backtracking
        """
        # build graph
        graph = dict()
        n = len(edges)
        for src, dst, time in edges:
            if src not in graph:
                graph[src] = []
            if dst not in graph:
                graph[dst] = []
            graph[src].append((dst, values[dst], time))
            graph[dst].append((src, values[src], time))
        # print(graph)
        visited = set()
        visited.add(0)
        self.backtracking(graph, visited, 0, values[0], 0, maxTime)
        return self.res
            


    def backtracking(self, graph, visited, node, quality, timeUsed, maxTime) -> None:
        if node == 0:
            self.res = max(self.res, quality)
        if node not in graph:
            return
        for neighbor,val,cost in graph[node]:
            if timeUsed + cost <= maxTime:
                if neighbor not in visited:
                    visited.add(neighbor)
                    self.backtracking(graph, visited, neighbor, quality + val, timeUsed + cost, maxTime)
                    visited.remove(neighbor)
                else:
                    self.backtracking(graph, visited, neighbor, quality, timeUsed+cost, maxTime)