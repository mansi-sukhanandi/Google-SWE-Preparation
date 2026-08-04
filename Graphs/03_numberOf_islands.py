class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
            
        ROWS, COLS = len(grid), len(grid[0])
        islands = 0
        
        def dfs(r, c):
            # Base Case: Out of bounds ya fir paani '0' aa gaya
            if r < 0 or r >= ROWS or c < 0 or c >= COLS or grid[r][c] == '0':
                return
            
            # Step 1: Is land ko sink (paani '0') kar do taaki repeat count na ho
            grid[r][c] = '0'
            
            # Step 2: Charo connected land addresses ko sink karo
            dfs(r + 1, c) # Down
            dfs(r - 1, c) # Up
            dfs(r, c + 1) # Right
            dfs(r, c - 1) # Left
        
        # Grid scan karo
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == '1':
                    islands += 1 # Naya island mila
                    dfs(r, c)    # Poore island ko '0' banakar sink kar do
                    
        return islands


