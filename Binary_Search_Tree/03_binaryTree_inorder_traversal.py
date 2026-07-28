class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        
        def dfs(node):
            if not node:
                return
            
            dfs(node.left)       # 1. Left Subtree
            res.append(node.val) # 2. Add Current Node Value
            dfs(node.right)      # 3. Right Subtree
            
        dfs(root)
        return res
