import heapq

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.minHeap = nums
        heapq.heapify(self.minHeap) # List ko Min-Heap banaya
        
        # Heap ka size hamesha 'k' ke equal rakho
        while len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)

    def add(self, val: int) -> int:
        # Naya element push karo
        heapq.heappush(self.minHeap, val)
        
        # Agar size 'k' se bada hua toh smallest element pop kar do
        if len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)
            
        # TOP par humara Kth Largest element hoga
        return self.minHeap[0]
