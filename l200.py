class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])
        res = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    res += 1
                    self.dfs(grid, i, j)
        return res
        
        
    def dfs(self, grid, i, j):
        """
        DFS the island('1') and change it to water('0')
        """
        m = len(grid)
        n = len(grid[0])
        if i < 0 or i > m - 1 or j < 0 or j > n - 1:
            return
            
        # already is water
        if grid[i][j] != '1':
            return
        
        # flood
        grid[i][j] = '0'
        for nexti, nextj in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]:
            self.dfs(grid, nexti, nextj)
        
        
        