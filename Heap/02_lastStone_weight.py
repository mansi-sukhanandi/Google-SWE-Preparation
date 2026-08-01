import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # Step 1: Max-Heap banane ke liye elements ko negative karo
        minHeap = [-s for s in stones]
        heapq.heapify(minHeap)
        
        # Step 2: Jab tak 2 ya usse zyada stones hain, smash karo
        while len(minHeap) > 1:
            first = heapq.heappop(minHeap)   # Sabse bada stone
            second = heapq.heappop(minHeap)  # Dusra sabse bada stone
            
            # Since numbers negative hain, first is actually smaller value wise 
            # e.g., -8 < -2 (meaning 8 > 2)
            if first != second:
                # bacha hua weight push karo
                heapq.heappush(minHeap, first - second)
                
        # Step 3: Result return karo
        return -minHeap[0] if minHeap else 0
