def bucketSort(arr):
    # 1. Empty Buckets banao
    bucket_count = 10
    buckets = [[] for _ in range(bucket_count)]
    
    # 2. Elements ko Buckets mein distribution karo
    max_val = max(arr) if arr else 1
    for num in arr:
        # Index calculation: Kaunsi bucket mein daalna hai
        index = (num * bucket_count) // (max_val + 1)
        buckets[index].append(num)
        
    # 3. Har bucket ko sort karo aur combine karo
    sorted_arr = []
    for b in buckets:
        sorted_arr.extend(sorted(b))
        
    return sorted_arr
