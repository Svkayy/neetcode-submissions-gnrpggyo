# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        count = 0
        def helper(tree):
            nonlocal count
            if not tree:
                return None
            
            left = helper(tree.left)
            if left:
                return left

            count += 1
            if count == k:
                return tree.val
            
            return helper(tree.right)
        
        return helper(root)