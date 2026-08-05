from collections import deque

def bfs(grid, start_r, start_c):
    ROWS, COLS = len(grid), len(grid[0])
    
    # Step 1: Queue banao aur start point daalo
    queue = deque([(start_r, start_c)])
    visited = set([(start_r, start_c)])
    
    # Step 2: Queue jab tak khali na ho
    while queue:
        r, c = queue.popleft() # Current address nikalo
        
        # 4 Directions
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        for dr, dc in directions:
            nr, nc = r + dr, c + dc # New neighbor address
            
            # Boundary & Valid Check
            if (0 <= nr < ROWS and 0 <= nc < COLS and 
                (nr, nc) not in visited and grid[nr][nc] != 0):
                
                queue.append((nr, nc))
                visited.add((nr, nc))
