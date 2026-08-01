import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # Step 1: Pehle k elements ka heap banao
        minHeap = nums[:k]
        heapq.heapify(minHeap)
        
        # Step 2: Remaining elements ke liye check karo
        for num in nums[k:]:
            if num > minHeap[0]:
                heapq.heappushpop(minHeap, num) # Push karo aur smallest ko pop kar do
                
        # Step 3: Root par kth largest element ready hai
        return minHeap[0]
