# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        """
        if not root:
            return None
        
        left = self.invertTree(root.left)
        right = self.invertTree(root.right)
        root.left = right 
        root.right = left
        return root
        """
        """
        if not root:
            return None

        stk = []
        stk.append(root)

        while stk:
            node = stk.pop()
            if node.left: stk.append(node.left)
            if node.right: stk.append(node.right)
            node.left, node.right = node.right, node.left
        
        return root
        """
        if not root:
            return None

        q = deque([root])
        while q:
            node = q.popleft()
            if node.right: q.append(node.right)
            if node.left: q.append(node.left)
            node.left, node.right = node.right, node.left

        return root 

