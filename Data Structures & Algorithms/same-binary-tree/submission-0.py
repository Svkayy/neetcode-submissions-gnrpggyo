# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        q = deque([p,q])
        while q:
            node1 = q.popleft()
            node2 = q.popleft()
            
            if node1 and node2:
                if node1.val != node2.val:
                    return False
            
            if node1 and not node2 or node2 and not node1:
                return False
            
            if node1 and node2:
                q.append(node1.left)
                q.append(node2.left)
                q.append(node1.right)
                q.append(node2.right)
        
        return True
                
        