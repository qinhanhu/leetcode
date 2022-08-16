class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m = len(board)
        n = len(board[0])
        visited = []
        for i in range(m):
            visited.append([False] * n)
        
        def dfs(board, x, y):
            nonlocal m, n
            if board[x][y] == 'O':
                board[x][y] = '#'
            else:
                return
            visited[x][y] = True
            for nx, ny in [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]:
                if 0 <= nx <= m - 1 and 0 <= ny <= n - 1 and not visited[nx][ny]:
                    dfs(board, nx, ny)
        
        for i in range(m):
            if not visited[i][0]:
                dfs(board, i, 0)
            if not visited[i][n-1]:
                dfs(board, i, n-1)
        
        for j in range(n):
            if not visited[0][j]:
                dfs(board, 0, j)
            if not visited[m-1][j]:
                dfs(board, m-1, j)
        
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                if board[i][j] == '#':
                    board[i][j] = 'O'        


