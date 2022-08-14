class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        path = []
        res = []
        def dfs(graph, node):
            path.append(node)
            if node == len(graph) - 1:
                res.append(path[:])
                #return
            for neighbor in graph[node]:
                dfs(graph, neighbor)
            path.pop()
        
        dfs(graph, 0)
        return res