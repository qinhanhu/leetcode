# https://leetcode.cn/problems/course-schedule-ii/
from collections import deque
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        """
        1. mark indegree of every nodes -> indegree[int]
        2. BFS start with nodes that has 0 indegree; if we visited all nodes, there is no loop in this graph, else it's impossible to finish all courses. Record the order when we visit nodes, return the order. 
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
        res = []
        while len(que) > 0:
            size = len(que)
            for _ in range(size):
                cur = que.popleft()
                res.append(cur)
                for neighbor in graph[cur]:
                    indegree[neighbor] -= 1
                    if indegree[neighbor] == 0:
                        que.append(neighbor)
            cnt += size
        
        if cnt != numCourses:
            return []
        return res