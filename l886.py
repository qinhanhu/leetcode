class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        graph = []
        for i in range(n):
            graph.append([])
        for src, to in dislikes:
            graph[src-1].append(to-1)
            graph[to-1].append(src-1)
        visited = [False] * n
        color = [0] * n
        isPossible = True
        def dfs(graph, node):
            nonlocal isPossible
            if not isPossible:
                return
            visited[node] = True
            for neighbor in graph[node]:
                if not visited[neighbor]:
                    color[neighbor] = 1 if color[node] == 0 else 0
                    dfs(graph, neighbor)
                else:
                    if color[neighbor] == color[node]:
                        isPossible = False
                        return
        
        for node in range(n):
            if not visited[node]:
                dfs(graph, node)
        return isPossible
                
            
