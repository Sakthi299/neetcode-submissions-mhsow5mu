class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.minStack and self.minStack[-1] <= val:
           # print("value of min 1st"+ str(self.minStack[-1]))
            self.minStack.append(self.minStack[-1])
        else:
            #print("value of min"+ str(val))
            self.minStack.append(val)

    def pop(self) -> None:
        if self.stack:
            self.stack = self.stack[:-1]
            #print("stack: " + str(self.stack))
        if self.minStack:
            self.minStack = self.minStack[:-1]
            #print("minstack :"+ str(self.stack))
        
    def top(self) -> int:
        if self.stack:
            return self.stack[-1]
        
    def getMin(self) -> int:
        return self.minStack[-1]
        
