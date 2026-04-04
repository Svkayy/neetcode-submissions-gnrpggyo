# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        diameter = 0
        def maxDepth(tree):
            nonlocal diameter
            if not tree:
                return 0
            
            left = maxDepth(tree.left)
            right = maxDepth(tree.right)

            diameter = max(left+right, diameter)

            return 1 + max(left, right)
        
        maxDepth(root)
        return diameter

