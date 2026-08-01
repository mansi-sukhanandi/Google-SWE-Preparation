import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: List[List[int]]) -> List[List[int]]:
        minHeap = []
        
        # Step 1: Har point ki distance calculate karke Heap array mein daalo
        for x, y in points:
            dist = (x ** 2) + (y ** 2)
            minHeap.append((dist, x, y))
            
        # Step 2: Heapify in O(N) time
        heapq.heapify(minHeap)
        
        # Step 3: Top k closest points pop kar lo
        res = []
        for _ in range(k):
            dist, x, y = heapq.heappop(minHeap)
            res.append([x, y])
            
        return res
