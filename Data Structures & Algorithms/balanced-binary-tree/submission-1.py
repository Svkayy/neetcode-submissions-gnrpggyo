# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        flag = True
        def maxDepth(tree):
            nonlocal flag
            if not tree:
                return 0

            left = maxDepth(tree.left)
            right = maxDepth(tree.right)

            if abs(left - right) > 1:
                flag = False


            return 1 + max(left, right)
        
        maxDepth(root)
        return flag