# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def check(tree, lo, hi):
            if not tree:
                return True

            if not lo < tree.val < hi:
                return False

            return check(tree.left, lo, tree.val) and check(tree.right, tree.val, hi)
        
        return check(root, float('-inf'), float('inf'))