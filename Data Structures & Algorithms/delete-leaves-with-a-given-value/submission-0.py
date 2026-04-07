# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        
        def dfs(tree):
            if not tree:
                return None
            
            tree.left = dfs(tree.left)
            tree.right = dfs(tree.right)

            if tree.val == target and not tree.left and not tree.right:
                return None
            
            return tree
        
        root = dfs(root)
        return root
        