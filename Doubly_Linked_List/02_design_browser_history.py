class BrowserHistory:
    def __init__(self, homepage: str):
        # Homepage ka pehla node aur current pointer setup
        self.curr = Node(homepage)

    def visit(self, url: str) -> None:
        # Naya node banayein aur connections establish karein
        new_node = Node(url)
        self.curr.next = new_node
        new_node.prev = self.curr
        # Current pointer ko nayi URL par shift karein
        self.curr = new_node

    def back(self, steps: int) -> str:
        # Peeche ki taraf walk karein jab tak steps hain aur prev node exist karta hai
        while steps > 0 and self.curr.prev:
            self.curr = self.curr.prev
            steps -= 1
        return self.curr.val

    def forward(self, steps: int) -> str:
        # Aage ki taraf walk karein jab tak steps hain aur next node exist karta hai
        while steps > 0 and self.curr.next:
            self.curr = self.curr.next
            steps -= 1
        return self.curr.val
