from collections import deque

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        res = []
        q = deque([root])
        
        while q:
            rightNode = None
            level_len = len(q)
            
            for i in range(level_len):
                node = q.popleft()
                if node:
                    rightNode = node # Har node update hoga, aakhiri waala rightmost bachega
                    if node.left:
                        q.append(node.left)
                    if node.right:
                        q.append(node.right)
            
            # Level ka sabse last node result mein append kar do
            if rightNode:
                res.append(rightNode.val)
                
        return res
