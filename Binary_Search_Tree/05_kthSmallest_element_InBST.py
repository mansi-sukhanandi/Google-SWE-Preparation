class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        res = []
        
        def inorder(node):
            if not node:
                return
            
            inorder(node.left)   # Left
            res.append(node.val) # Root
            inorder(node.right)  # Right
            
        inorder(root)
        
        return res[k - 1]
