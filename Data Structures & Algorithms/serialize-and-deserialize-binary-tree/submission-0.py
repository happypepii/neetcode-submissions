# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    def _preorder(self, node, result):
        if node is None:
            result.append("null")
            return
        result.append(str(node.val))
        self._preorder(node.left, result)
        self._preorder(node.right, result)
    # Encodes a tree to a single string.
    def serialize(self, root):
        result = []
        self._preorder(root, result)
        return ",".join(result)
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        vals = data.split(",")
        self.index = 0

        def build() -> Optional[TreeNode]:
            val = vals[self.index]
            self.index += 1              # 讀完一個,往後移
            if val == "null":
                return None              # 終止條件
            node = TreeNode(int(val))
            node.left = build()          # 左子樹會把 index 往前推
            node.right = build()         # 接著從左子樹讀完的位置繼續
            return node

        return build()
    

