def mergeKLists(lists):
    if not lists or len(lists) == 0:
        return None
    
    # Jab tak 1 se zyada lists hain, pairs banakar merge karte raho
    while len(lists) > 1:
        merged_lists = []
        
        # 2-2 ke step se aage badho (i, i+1)
        for i in range(0, len(lists), 2):
            l1 = lists[i]
            # Agar i+1 index par list hai toh l2 wo hoga, nahi toh None
            l2 = lists[i + 1] if (i + 1) < len(lists) else None
            
            # Dono ko merge karke humari temporary array mein daal do
            merged_lists.append(mergeTwoLists(l1, l2))
            
        lists = merged_lists  # Lists ko update kar do
        
    return lists[0]  # Final 1 bachi hui list return kar do!
