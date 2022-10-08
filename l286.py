class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        """
        BFS from all gates at the same time
        Time: O(mn)
        Space: O(mn) queue's size
        
        """
        INF = 2**31 - 1
        queue = collections.deque()
        m = len(rooms)
        n = len(rooms[0])
        visited = set()
        for i in range(m):
            for j in range(n):
                if rooms[i][j] == 0:
                    queue.append((i, j))
                    visited.add((i, j))
        
        distance = 0
        while len(queue) > 0:
            size = len(queue)
            for _ in range(size):
                i, j = queue.popleft()
                rooms[i][j] = distance
                for nexti, nextj in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]:
                    if 0 <= nexti <= m-1 and 0 <= nextj <= n-1 and rooms[nexti][nextj] == INF and (nexti, nextj) not in visited:
                        queue.append((nexti, nextj))
                        visited.add((nexti, nextj))
            distance += 1
        