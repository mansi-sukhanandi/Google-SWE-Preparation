class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        M, N = len(text1), len(text2)
        # 2D DP Table initialized with 0s
        dp = [[0] * (N + 1) for _ in range(M + 1)]

        # Bottom-Up Fill
        for i in range(M - 1, -1, -1):
            for j in range(N - 1, -1, -1):
                if text1[i] == text2[j]:
                    dp[i][j] = 1 + dp[i + 1][j + 1] # Match!
                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j + 1]) # Mismatch!

        return dp[0][0]

