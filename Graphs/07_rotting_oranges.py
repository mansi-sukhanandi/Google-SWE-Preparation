from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        queue = deque()
        fresh = 0
        minutes = 0

        # Step 1: Sade hue santron ko Queue mein daalo aur Fresh count karo
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    queue.append((r, c))
                elif grid[r][c] == 1:
                    fresh += 1

        # Direct return agar koi fresh santra hai hi nahi
        if fresh == 0:
            return 0

        # Step 2: Multi-Source BFS Spreading
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        while queue and fresh > 0:
            # Current minute par kitne rotten oranges hain
            for _ in range(len(queue)):
                r, c = queue.popleft()

                for dr, dc in directions:
                    nr, nc = r + dr, c + dc

                    # Boundary check aur agar Fresh santra mila
                    if 0 <= nr < ROWS and 0 <= nc < COLS and grid[nr][nc] == 1:
                        grid[nr][nc] = 2 # Sada do!
                        queue.append((nr, nc))
                        fresh -= 1 # Ek fresh kam hua

            minutes += 1 # Ek minute beet gaya

        # Step 3: Check karo saare sade ya nahi
        return minutes if fresh == 0 else -1
