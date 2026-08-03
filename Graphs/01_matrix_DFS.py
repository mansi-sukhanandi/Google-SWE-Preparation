def dfs(grid, r, c, visited):
    ROWS, COLS = len(grid), len(grid[0])
    
    # Rule 1: Out of Bounds or already visited / blocked check
    if (r < 0 or c < 0 or 
        r >= ROWS or c >= COLS or 
        (r, c) in visited or grid[r][c] == 0):
        return
    
    # Rule 2: Mark visited
    visited.add((r, c))
    
    # Rule 3: 4 Directions mein DFS call
    dfs(grid, r + 1, c, visited) # Down
    dfs(grid, r - 1, c, visited) # Up
    dfs(grid, r, c + 1, visited) # Right
    dfs(grid, r, c - 1, visited) # Left
