class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> List[List[int]]:
        M, N = len(obstacleGrid), len(obstacleGrid[0])
        
        # Edge Case: Start ya End par hi obstacle hai
        if obstacleGrid[0][0] == 1 or obstacleGrid[M-1][N-1] == 1:
            return 0
            
        dp = [[0] * N for _ in range(M)]
        dp[0][0] = 1 # Start point

        for r in range(M):
            for c in range(N):
                # Agar cell obstacle hai, toh skipped
                if obstacleGrid[r][c] == 1:
                    dp[r][c] = 0
                    continue
                    
                # Upar wali cell se paths add karo
                if r > 0:
                    dp[r][c] += dp[r - 1][c]
                # Left wali cell se paths add karo
                if c > 0:
                    dp[r][c] += dp[r][c - 1]

        return dp[M - 1][N - 1]
