# DFS
# class Solution:
#     def isBipartite(self, graph: List[List[int]]) -> bool:
#         flag = True
#         visited = [False] * len(graph)
#         color = [0] * len(graph)
#         def dfs(graph, node):
#             nonlocal flag
#             if flag == False:
#                 return
#             visited[node] = True
#             for neighbor in graph[node]:
#                 if not visited[neighbor]:
#                     if color[node] == 0:
#                         color[neighbor] = 1
#                     else:
#                         color[neighbor] = 0
#                     dfs(graph, neighbor)
#                 else:
#                     if color[neighbor] == color[node]:
#                         flag = False
#                         return
#         for node in range(len(graph)):
#             if not visited[node]:
#                 dfs(graph, node)
#         return flag
                    

# BFS
from collections import deque
class Solution:
    def isBipartite(self, graph) -> bool:
        flag = True
        visited = [False] * len(graph)
        color = [0] * len(graph)
        def bfs(graph, node):
            nonlocal flag
            que = deque()
            que.append(node)
            visited[node] = True
            while len(que) > 0:
                size = len(que)
                for _ in range(size):
                    cur = que.popleft()
                    for neighbor in graph[cur]:
                        if not visited[neighbor]:
                            visited[neighbor] = True
                            color[neighbor] = 1 if color[cur] == 0 else 0
                            bfs(graph, neighbor)
                        else:
                            if color[neighbor] == color[cur]:
                                flag = False
                                return
        
        for node in range(len(graph)):
            if not visited[node]:
                bfs(graph, node)
        return flag

    def A(self):
        b = 1
        b = self.B(b)
        print(b)

    def B(self, val):
        val = 0
        return val


s = Solution()
s.A()


                        

                    
            

            
            