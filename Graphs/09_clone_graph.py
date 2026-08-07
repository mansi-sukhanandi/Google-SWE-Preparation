"""
# Node definition:
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return None
            
        old_to_new = {}

        def dfs(node):
            # Step 1: Agar copy pehle se bani hui hai, wahi return kar do
            if node in old_to_new:
                return old_to_new[node]

            # Step 2: Naya copy node banao
            copy = Node(node.val)
            old_to_new[node] = copy

            # Step 3: Saare neighbors ki copy bana kar link karo
            for neighbor in node.neighbors:
                copy.neighbors.append(dfs(neighbor))

            return copy

        return dfs(node)
