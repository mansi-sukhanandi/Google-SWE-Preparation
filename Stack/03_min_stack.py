class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val):
        # 1. Main stack mein value daal do
        self.stack.append(val)
        
        # 2. Min stack mein daalne ke liye naya minimum decide karo
        if self.min_stack:
            # Agar min_stack khali nahi hai, toh check karo dono mein se chota kaun hai
            new_min = min(val, self.min_stack[-1])
        else:
            # Agar min_stack khali hai (matlab yeh pehla element hai), toh yahi minimum hai
            new_min = val
            
        # Naya minimum min_stack mein push kar do
        self.min_stack.append(new_min)

    def pop(self):
        # Dono stack se ek-ek element nikal do
        self.stack.pop()
        self.min_stack.pop()

    def top(self):
        # Main stack ka sabse oopar wala element return karo
        return self.stack[-1]

    def getMin(self):
        # Min stack ka sabse oopar wala element hi humara sabse chota number hai
        return self.min_stack[-1]
