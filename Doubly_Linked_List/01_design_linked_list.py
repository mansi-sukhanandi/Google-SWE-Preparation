class Node:
    def __init__(self, val=0):
        self.val = val
        self.next = None
        self.prev = None

class MyLinkedList:
    def __init__(self):
        # Dummy Guard Nodes setup
        self.head = Node(0)
        self.tail = Node(0)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.length = 0

    # Helper function for insertion
    def _add_between(self, val: int, prev_node: Node, next_node: Node):
        new_node = Node(val)
        new_node.prev = prev_node
        new_node.next = next_node
        prev_node.next = new_node
        next_node.prev = new_node
        self.length += 1

    def get(self, index: int) -> int:
        if index < 0 or index >= self.length:
            return -1
        curr = self.head.next
        for _ in range(index):
            curr = curr.next
        return curr.val

    def addAtHead(self, val: int) -> None:
        self._add_between(val, self.head, self.head.next)

    def addAtTail(self, val: int) -> None:
        self._add_between(val, self.tail.prev, self.tail)

    def addAtIndex(self, index: int, val: int) -> None:
        if index < 0 or index > self.length:
            return
        
        # Jis index par daalna hai, uske pichle aur agle node ko dhoondho
        prev_node = self.head
        for _ in range(index):
            prev_node = prev_node.next
        next_node = prev_node.next
        
        self._add_between(val, prev_node, next_node)

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.length:
            return
        
        # Target node tak pahuche
        curr = self.head.next
        for _ in range(index):
            curr = curr.next
          
        prev_node = curr.prev
        next_node = curr.next
        
        prev_node.next = next_node
        next_node.prev = prev_node
        
        self.length -= 1
