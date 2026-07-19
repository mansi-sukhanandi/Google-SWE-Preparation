class Solution:
    def mergeTwoLists(self, list1, list2):
        # 1. Ek dummy node banaya taaki shuruat aasan ho
        dummy = ListNode(0)
        tail = dummy
        
        l1 = list1
        l2 = list2
        
        # 2. Jab tak dono lists mein elements hain
        while l1 and l2:
            if l1.val < l2.val:
                tail.next = l1
                l1 = l1.next  # List 1 mein aage badho
            else:
                tail.next = l2
                l2 = l2.next  # List 2 mein aage badho
                
            tail = tail.next  # Nayi list ka tail aage badhao
            
        # 3. Agar koi ek list bach gayi hai, toh use direct jod do
        if l1:
            tail.next = l1
        elif l2:
            tail.next = l2
            
        return dummy.next  # Dummy ke aage se hamari asli sorted list shuru hai!
