class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        # Base Case 1: Empty Tree
        if not root:
            return False
        
        # Base Case 2: Agar hum Leaf Node par pahunch gaye
        if not root.left and not root.right:
            return root.val == targetSum
        
        # Recursive Step: Target ko reduce kar ke Left aur Right check karo
        newTarget = targetSum - root.val
        
        return self.hasPathSum(root.left, newTarget) or self.hasPathSum(root.right, newTarget)
