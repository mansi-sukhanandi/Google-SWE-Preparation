def searchRange(nums, target):
    def findBound(isFirst):
        L, R = 0, len(nums) - 1
        bound = -1
        
        while L <= R:
            M = L + (R - L) // 2
            if nums[M] == target:
                bound = M
                if isFirst:
                    R = M - 1  # Left mein search zari rakho
                else:
                    L = M + 1  # Right mein search zari rakho
            elif target > nums[M]:
                L = M + 1
            else:
                R = M - 1
                
        return bound

    return [findBound(True), findBound(False)]
