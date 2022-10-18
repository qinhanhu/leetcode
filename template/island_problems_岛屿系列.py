# Island Problems

# Flood Fill 遍历并淹没岛屿, 不需要visited数组, O(1) space
def dfs(grid, i, j):
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
        dfs(grid, nexti, nextj)

# 不淹没岛屿，需要带visited数组避免重复遍历
def dfs(grid, i, j, visited):
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

    if (i, j) in visited:
    	return

    visited.add((i, j))
    # flood
    grid[i][j] = '0'
    for nexti, nextj in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]:
        dfs(grid, nexti, nextj, visited)