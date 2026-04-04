# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        count = 0
        def countNodes(tree, val):
            nonlocal count
            if not tree:
                return 
            if tree.val >= val:
                count += 1
            newVal = max(tree.val, val)
            countNodes(tree.left, newVal)
            countNodes(tree.right, newVal)
        
        countNodes(root, root.val)
        return count
        