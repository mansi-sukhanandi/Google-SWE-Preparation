class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        # 1. Base Case: Agar space khali mil jaye
        if not root:
            return TreeNode(val)
        
        # 2. Agar value chhoti hai -> Left side jao
        if val < root.val:
            root.left = self.insertIntoBST(root.left, val)
            
        # 3. Agar value badi hai -> Right side jao
        else:
            root.right = self.insertIntoBST(root.right, val)
            
        return root
