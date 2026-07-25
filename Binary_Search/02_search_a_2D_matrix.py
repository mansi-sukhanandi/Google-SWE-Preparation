def searchMatrix(matrix, target):
    if not matrix:
        return False
        
    rows, cols = len(matrix), len(matrix[0])
    L, R = 0, (rows * cols) - 1
    
    while L <= R:
        M = L + (R - L) // 2
        # 1D index M ko 2D cell mein convert karo
        row, col = M // cols, M % cols
        val = matrix[row][col]
        
        if val == target:
            return True
        elif target > val:
            L = M + 1
        else:
            R = M - 1
            
    return False
