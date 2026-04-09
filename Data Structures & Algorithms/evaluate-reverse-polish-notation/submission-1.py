class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for num in tokens:

            if num in ["+", "-", "*", "/"] and len(stack) > 1:
                val1 = int(stack.pop())
                val2 = int(stack.pop())
                if num == "+":
                    exp = val2 + val1 
                if num == "-":
                    exp = val2 - val1 
                if num == "*":
                    exp = val2 * val1 
                if num == "/":
                    exp = val2 / val1
                stack.append(exp) 
            else:
                stack.append(num)
        
        return int(stack[-1])