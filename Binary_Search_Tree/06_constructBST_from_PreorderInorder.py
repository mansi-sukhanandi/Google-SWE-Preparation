class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # Base Case: Agar list khali ho jaye
        if not preorder or not inorder:
            return None
        
        # 1. Preorder ka pehla element hi Root hai
        rootVal = preorder[0]
        root = TreeNode(rootVal)
        
        # 2. Inorder mein rootVal ka index dhoondho
        mid = inorder.index(rootVal)
        
        # 3. Recursive Calls
        # Left Subtree ke liye preorder aur inorder slice karke bhej do
        root.left = self.buildTree(preorder[1 : mid + 1], inorder[:mid])
        
        # Right Subtree ke liye baaki bacha hua bhej do
        root.right = self.buildTree(preorder[mid + 1 :], inorder[mid + 1 :])
        
        return root
