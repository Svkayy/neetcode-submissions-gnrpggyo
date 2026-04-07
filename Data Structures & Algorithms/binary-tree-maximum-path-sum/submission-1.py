# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        m = float('-inf')
        def dfs(tree):
            nonlocal m
            if not tree:
                return 0
            
            left = max(0, dfs(tree.left))
            right = max(0, dfs(tree.right))
            m = max(m, (left + tree.val + right))

            return tree.val + max(left, right)
        
        dfs(root)
        return m
