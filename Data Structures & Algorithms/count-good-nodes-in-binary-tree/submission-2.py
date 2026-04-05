# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        count = 0
        def helper(tree, val):
            nonlocal count
            if not tree:
                return
            
            if tree.val >= val:
                count += 1
            
            val = max(tree.val, val)
            helper(tree.left, val)
            helper(tree.right, val)
        
        helper(root, root.val)
        return count