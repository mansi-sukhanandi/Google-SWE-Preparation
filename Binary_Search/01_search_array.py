def search(nums, target):
    L, R = 0, len(nums) - 1
    while L <= R:
        M = L + (R - L) // 2
        if nums[M] == target:
            return M
        elif target > nums[M]:
            L = M + 1
        else:
            R = M - 1
    return -1
