# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        """
        # Recursive DFS
        if not root:
            return 0
        maxLeft = self.maxDepth(root.left)
        maxRight = self.maxDepth(root.right)
        
        return 1 + max(maxLeft,maxRight)
        """

        """
        # Iterative BFS
        if not root:
            return 0
        q = deque()
        q.append(root) 
        # q = deque([root])
        level = 0

        while q:
            q_length = len(q)
            for _ in range(q_length):
                node = q.popleft()
                if node.left: q.append(node.left)
                if node.right: q.append(node.right)
            level += 1
        
        return level
        """

        # Iterative DFS - preorder

        if not root:
            return 0
        
        res = 1
        stack = [(root,1)]

        while stack:
            node, depth = stack.pop()
            res = max(depth, res)
            #print(node.val, depth)
            if node.right: stack.append((node.right,depth+1))
            if node.left: stack.append((node.left,depth+1))
             
        return res




