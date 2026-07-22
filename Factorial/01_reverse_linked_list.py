class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head
        
        while curr:
            nxt = curr.next     # 1. Aage ka node save kiya
            curr.next = prev    # 2. Arrow ulta ghumaya
            prev = curr         # 3. prev ko ek step aage laye
            curr = nxt          # 4. curr ko ek step aage laye
            
        return prev  # Jab loop khatam hoga, prev hi hamara NAYA HEAD hoga!
