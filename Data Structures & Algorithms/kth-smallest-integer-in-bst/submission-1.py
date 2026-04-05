# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        counter = k
        res = 0
        def helper(tree, j):
            nonlocal counter, res
            if not tree:
                return 
            
            helper(tree.left, counter)

            counter -= 1
            if counter == 0:
                res = tree.val
                return

            
            helper(tree.right, counter)
        
        helper(root, k)
        return res
            
