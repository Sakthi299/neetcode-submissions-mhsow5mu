class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = []

        for i, j in zip(position, speed):
            pairs.append([i,j])

        pairs.sort()

        stack = []
        for p, s in pairs[::-1]:
            stack.append((target-p)/s)
            if len(stack) > 1 and stack[-1] <= stack[-2]:
                stack.pop()
            
        return len(stack)