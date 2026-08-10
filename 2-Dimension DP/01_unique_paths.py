class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # Step 1: 2D Matrix initialize karo with 1s
        dp = [[1] * n for _ in range(m)]
        
        # Step 2: Fill Grid (Skip first row & first col as they only have 1 way)
        for r in range(1, m):
            for c in range(1, n):
                dp[r][c] = dp[r - 1][c] + dp[r][c - 1]
                
        return dp[m - 1][n - 1]
