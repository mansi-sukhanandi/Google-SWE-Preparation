class Solution:
    def reverseList(self, head):
        prev = None
        curr = head
        
        while curr:
            nxt = curr.next     # 1. Agla dabba safe kiya
            curr.next = prev    # 2. Arrow ulta ghumaya
            prev = curr         # 3. Prev ko aage badhaya
            curr = nxt          # 4. Curr ko aage badhaya
            
        return prev  
