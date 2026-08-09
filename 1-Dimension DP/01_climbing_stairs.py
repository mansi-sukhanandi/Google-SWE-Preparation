class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
            
        # dp[i] represents number of ways to reach step i
        dp = [0] * (n + 1)
        dp[1] = 1 # Step 1 tak pahunchne ka 1 tarika
        dp[2] = 2 # Step 2 tak pahunchne ke 2 tarike (1+1 ya direct 2)
        
        for i in range(3, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
            
        return dp[n]
