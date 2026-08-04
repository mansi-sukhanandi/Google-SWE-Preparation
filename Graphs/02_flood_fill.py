class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        ROWS, COLS = len(image), len(image[0])
        oldColor = image[sr][sc]
        
        # Agar start point pehle se target color hai, toh return kar do
        if oldColor == color:
            return image
        
        def dfs(r, c):
            # Base Case: Matrix se bahar chale gaye ya color purane wale se alag hai
            if r < 0 or r >= ROWS or c < 0 or c >= COLS or image[r][c] != oldColor:
                return
            
            # Step 1: Naya color paint karo
            image[r][c] = color
            
            # Step 2: Charo neighboring addresses par paint phelao
            dfs(r + 1, c) # Down
            dfs(r - 1, c) # Up
            dfs(r, c + 1) # Right
            dfs(r, c - 1) # Left
            
        # Paint Bucket Start!
        dfs(sr, sc)
        
        return image
