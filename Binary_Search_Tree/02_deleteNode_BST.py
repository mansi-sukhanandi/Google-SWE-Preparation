class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return None
        
        # 1. Target node tak pohocho
        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        else:
            # 2. Target Node MIL GAYI!
            
            # Case 1 & 2: 0 ya 1 child
            if not root.left:
                return root.right
            if not root.right:
                return root.left
            
            # Case 3: 2 children
            # Right Subtree ka minimum node dhoondho
            minNode = root.right
            while minNode.left:
                minNode = minNode.left
                
            # Value overwrite kar do
            root.val = minNode.val
            
            # Ab right subtree se duplicate value delete kar do
            root.right = self.deleteNode(root.right, minNode.val)
            
        return root
