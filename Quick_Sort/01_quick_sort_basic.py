def quick_sort(arr):
    # Base Case: Agar array mein 0 ya 1 element hai, toh wo pehle se sorted hai!
    if len(arr) <= 1:
        return arr
    
    # 1. Pivot choose karo (aakhri element)
    pivot = arr[-1]
    
    # 2. Partitioning karo: Chhote aur Bade elements alag karo
    left = [x for x in arr[:-1] if x <= pivot]  # Chhote elements
    right = [x for x in arr[:-1] if x > pivot]   # Bade elements
    
    # 3. Recursive call aur Combine!
    return quick_sort(left) + [pivot] + quick_sort(right)
