# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
from typing import Optional, List

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []

        result = []
        q = deque([root])

        while q:
            level_size = len(q)   # 這一層有幾個節點
            l = []
            for _ in range(level_size):
                item = q.popleft()
                l.append(item.val)
                if item.left:
                    q.append(item.left)
                if item.right:
                    q.append(item.right)
            result.append(l)

        return result