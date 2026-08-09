class Solution:
    def rob(self, nums: List[int]) -> int:
        rob1, rob2 = 0, 0
        
        # Array iteration: [rob1, rob2, n, n+1, ...]
        for n in nums:
            # Maximise: Current + rob1 (two steps back) vs rob2 (one step back)
            temp = max(n + rob1, rob2)
            rob1 = rob2
            rob2 = temp
            
        return rob2
