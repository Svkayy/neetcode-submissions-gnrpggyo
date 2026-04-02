from collections import deque

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot: return True
        if not root: return False

        def isSame(s, t):
            if not s and not t: return True
            if not s or not t: return False
            if s.val != t.val: return False
            return isSame(s.left, t.left) and isSame(s.right, t.right)

        if isSame(root, subRoot):
            return True
        
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)