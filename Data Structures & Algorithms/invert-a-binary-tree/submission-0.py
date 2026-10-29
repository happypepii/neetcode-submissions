# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def swap(root: Optional[TreeNode]):
    temp = root.left
    root.left = root.right
    root.right = temp

def Invert(root: Optional[TreeNode]):
    if root is None:
        return

    Invert(root.left)
    Invert(root.right)
    swap(root)



class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        Invert(root)
        return root
        