class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        sol = []
        
        def backtrack(i):
            # Base Case: Jab saare elements process ho jayein
            if i >= len(nums):
                res.append(sol.copy()) # sol ka clone daal do
                return
            
            # Choice 1: Include nums[i]
            sol.append(nums[i])
            backtrack(i + 1)
            
            # Backtrack (Choice undo karo)
            sol.pop()
            
            # Choice 2: Exclude nums[i]
            backtrack(i + 1)
            
        backtrack(0)
        return res
