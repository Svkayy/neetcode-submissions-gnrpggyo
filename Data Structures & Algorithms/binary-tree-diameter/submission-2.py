# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        length = float('-inf')
        def diameter(tree):
            nonlocal length
            if not tree:
                return 0
            
            left = diameter(tree.left)
            right = diameter(tree.right)
            length = max(length, left + right)

            return 1 + max(left, right)
        
        diameter(root)

        if length == float('-inf'):
            return 0
        return length