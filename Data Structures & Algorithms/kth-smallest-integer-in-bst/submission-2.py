class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        counter = k
        def helper(tree, j):
            nonlocal counter
            if not tree:
                return None
            
            left_res = helper(tree.left, counter)
            if left_res is not None:
                return left_res

            counter -= 1
            if counter == 0:
                return tree.val

            return helper(tree.right, counter)
        
        
        return helper(root, k)