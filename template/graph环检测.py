# BFS
from collections import deque
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        """
        1. mark indegree of every nodes -> indegree[int]
        2. BFS from nodes that has 0 indegree; if we could visit all nodes, there is no loop in this graph
        """
        
        # step 1
        # build graph
        graph = []
        for i in range(numCourses):
            graph.append([])
        indegree = [0] * numCourses
        for dst, src in prerequisites:
            graph[src].append(dst)
            indegree[dst] += 1
        # step 2
        que = deque()
        for i, val in enumerate(indegree):
            if val == 0:
                que.append(i)
        # print(que, graph)
        cnt = 0
        while len(que) > 0:
            size = len(que)
            for _ in range(size):
                cur = que.popleft()
                for neighbor in graph[cur]:
                    indegree[neighbor] -= 1
                    if indegree[neighbor] == 0:
                        que.append(neighbor)
            cnt += size
        # print(cnt)
        return cnt == numCourses

# DFS
class Solution:
    def __init__(self):
        self.visited = []
        self.onpath = []
        self.hasCircle = False
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # build graph
        graph = []
        for i in range(numCourses):
            graph.append([])
        for dst, src in prerequisites:
            graph[src].append(dst)
        # print(graph)
        self.visited = [0] * numCourses
        self.onpath = [0] * numCourses
        for i in range(numCourses):
            self.dfs(graph,i)
        return not self.hasCircle
        
    def dfs(self, graph, node):
        if self.onpath[node] == 1:
            self.hasCircle = True
            return
        if self.visited[node] or self.hasCircle:
            return
        self.visited[node] = 1
        self.onpath[node] = 1
        for neighbor in graph[node]:
            self.dfs(graph, neighbor)
        self.onpath[node] = 0