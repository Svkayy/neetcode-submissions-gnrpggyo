# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        m = 0
        def maxLength(root):
            nonlocal m
            if not root:
                return 0
            
            left = maxLength(root.left)
            right = maxLength(root.right)
            m = max(m, left + right)

            return 1 + max(left, right)
        
        maxLength(root)
        return m