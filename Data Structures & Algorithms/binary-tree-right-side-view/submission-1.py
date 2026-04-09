# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        q = deque([root])
        res = []
        res.append(root.val)

        while q:
            levelSet = False
            for _ in range(len(q)):
                node = q.popleft()
                if node.right: 
                    q.append(node.right)
                if node.left:
                    q.append(node.left)
                #if not node.right and not node.left:
                #    res.append(node)
                if not levelSet and node.right:
                    res.append(node.right.val)
                    levelSet = True
                elif not levelSet and not node.right and node.left:
                    res.append(node.left.val)
                    levelSet = True
                
        return res
                
                
