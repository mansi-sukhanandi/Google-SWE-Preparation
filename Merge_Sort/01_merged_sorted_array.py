def merge(nums1, m, nums2, n):
    # Pointers set kar do piche se!
    p1 = m - 1        # nums1 ke real elements ka last
    p2 = n - 1        # nums2 ka last
    p = m + n - 1     # nums1 ka actual last (jahan zeroes hain)
    
    # Backwards Battle!
    while p1 >= 0 and p2 >= 0:
        if nums1[p1] > nums2[p2]:
            nums1[p] = nums1[p1]
            p1 -= 1
        else:
            nums1[p] = nums2[p2]
            p2 -= 1
        p -= 1
        
    # Agar nums2 mein abhi bhi elements bache hain
    while p2 >= 0:
        nums1[p] = nums2[p2]
        p2 -= 1
        p -= 1
