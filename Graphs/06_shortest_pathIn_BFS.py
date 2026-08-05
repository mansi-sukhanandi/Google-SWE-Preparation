from collections import deque

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        N = len(grid)
        
        # Edge case: Start ya End blocked hai
        if grid[0][0] == 1 or grid[N-1][N-1] == 1:
            return -1
            
        # Queue stores: (row, col, path_length)
        queue = deque([(0, 0, 1)])
        grid[0][0] = 1 # Mark as visited by blocking
        
        # 8 Directions
        directions = [
            (-1, -1), (-1, 0), (-1, 1),
            (0, -1),           (0, 1),
            (1, -1),  (1, 0),  (1, 1)
        ]
        
        while queue:
            r, c, length = queue.popleft()
            
            # Destination reached!
            if r == N - 1 and c == N - 1:
                return length
                
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                
                # Check valid address and open path (0)
                if 0 <= nr < N and 0 <= nc < N and grid[nr][nc] == 0:
                    queue.append((nr, nc, length + 1))
                    grid[nr][nc] = 1 # Mark visited
                    
        return -1
