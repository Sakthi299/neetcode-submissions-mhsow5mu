from collections import deque

class stackDeque:
    def __init__(self):
        self.items = deque()
    def is_empty(self):
        if len(self.items) == 0:
            return True
        return False
    def peek(self):
        if self.is_empty():
            return None
        return self.items[-1] 
    def push(self, item):
        self.items.append(item)
    def pop(self):
        if self.is_empty():
            return "Stack Empty"
        self.items.pop()


class Solution:
    def isValid(self, s: str) -> bool:
        bracStack = stackDeque()
        #print(bracStack.is_empty())
        #return True
    
        for char in s:
            if char == '(' or char == '{' or char == '[':
                bracStack.push(char)
            else: 
                if char  == ')' and bracStack.peek() != '(':
                    return False
                if char == '}' and bracStack.peek() != '{':
                    return False
                if char == ']' and bracStack.peek() != '[':
                    return False
                #print()
                bracStack.pop()
        if bracStack.is_empty():
            return True
        else:
            return False 
        







        