class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def checkHeight(node):
            if not node:
                return 0
            
            # Left Subtree check karo
            leftHeight = checkHeight(node.left)
            if leftHeight == -1: 
                return -1
            
            # Right Subtree check karo
            rightHeight = checkHeight(node.right)
            if rightHeight == -1: 
                return -1
            
            # Unbalance condition check
            if abs(leftHeight - rightHeight) > 1:
                return -1
            
            # Agar sab sahi hai toh normal height return karo
            return 1 + max(leftHeight, rightHeight)
        
        # main function return karega True agar result -1 NAHI hai
        return checkHeight(root) != -1
