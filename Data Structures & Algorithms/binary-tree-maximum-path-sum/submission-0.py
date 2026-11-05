# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        global_max = -math.inf

        def dfs(node):
            nonlocal global_max
            if node is None:
                return 0
            
            leftV = max(dfs(node.left), 0)
            rightV = max(dfs(node.right), 0)
            global_max = max(node.val + leftV + rightV, global_max)

            return node.val + max(leftV, rightV)

        dfs(root)
        return global_max