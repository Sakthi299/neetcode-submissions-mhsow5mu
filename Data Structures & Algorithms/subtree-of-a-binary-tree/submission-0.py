# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def sameTree(self, t1, t2):
            if not t1 and not t2:
                return True
            if not t1 or not t2 or t1.val != t2.val:
                return False
            
            left = self.sameTree(t1.left, t2.left)
            right = self.sameTree(t1.right, t2.right)

            return left and right

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot:
            return True
        if not root:
            return False
        
        if self.sameTree(root, subRoot):
            return True
        
        leftR = self.isSubtree(root.left, subRoot)
        rightR = self.isSubtree(root.right, subRoot)

        return (leftR or rightR)
