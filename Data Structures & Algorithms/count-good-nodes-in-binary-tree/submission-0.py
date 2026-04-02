# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        count = 0
        q = deque([(root, root.val)])
        while q:
            curr, pathmax = q.popleft()
            if curr.val >= pathmax:
                count += 1
            pathmax = max(curr.val, pathmax)
            if curr.left:
                q.append((curr.left, pathmax))
            if curr.right:
                q.append((curr.right, pathmax))
            
        return count
        