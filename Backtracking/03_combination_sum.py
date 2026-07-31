class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        sol = []
        
        def backtrack(i, current_sum):
            # Base Case 1: Target achieve ho gaya!
            if current_sum == target:
                res.append(sol.copy())
                return
            
            # Base Case 2: Out of bounds ya sum target se bada ho gaya
            if i >= len(candidates) or current_sum > target:
                return
            
            # Choice 1: Include candidates[i] (same index 'i' par bane raho)
            sol.append(candidates[i])
            backtrack(i, current_sum + candidates[i])
            
            # Backtrack (Undo decision)
            sol.pop()
            
            # Choice 2: Exclude candidates[i] (aage badho 'i + 1')
            backtrack(i + 1, current_sum)
            
        backtrack(0, 0)
        return res
