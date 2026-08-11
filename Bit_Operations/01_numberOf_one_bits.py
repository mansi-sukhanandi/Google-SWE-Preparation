class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        while n > 0:
            n = n & (n - 1)  # Rightmost set bit ko zero karta hai
            count += 1
        return count
