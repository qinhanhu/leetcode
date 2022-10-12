class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        res = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    for nexti, nextj in [(i, j+1),(i, j-1),(i+1, j), (i-1, j)]:
                        if 0<=nexti<=m-1 and 0<=nextj<=n-1 and grid[nexti][nextj] == 1:
                            continue
                        res += 1
        return res