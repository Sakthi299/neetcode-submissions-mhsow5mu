from collections import deque

class StackDeque:
    def __init__(self):
        self.items = deque()
    def is_empty(self):
        if len(self.items) == 0:
            return True
        return False
    def push(self, item):
        self.items.append(item)
    def peek(self):
        if self.is_empty():
            return None
        return self.items[-1]
    def pop(self):
        if self.is_empty():
            raise IndexError("stack empty")
        self.items.pop() 

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) == len(t):
            stack = StackDeque()
            s = "".join(sorted(s))
            #print(s)
            t = "".join(sorted(t, reverse=True))
            #print(t)
            for char in s:
                stack.push(char)
                #print(char)
            for char in t:
                if char == stack.peek():
                    #print(char)
                    stack.pop()
                else:
                    return False

            #print(stack.is_empty())
            return True
        else:
            return False