# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        
        if not p or not q:
            return False

        qu = deque([p, q])
        while qu:
            t1 = qu.popleft()
            t2 = qu.popleft()

            if t1.val != t2.val:
                return False
            if t1.left and not t2.left or t2.left and not t1.left:
                return False
            if t1.right and not t2.right or t2.right and not t1.right:
                return False

            if t1.left and t2.left:
                qu.append(t1.left)
                qu.append(t2.left)

            if t1.right and t2.right:
                qu.append(t1.right)
                qu.append(t2.right)
        
        return True

        