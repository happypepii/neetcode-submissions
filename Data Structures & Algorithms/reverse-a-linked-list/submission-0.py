# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None

        curr = head           # 站在已處理的最前面 (一開始是 0)
        nxt = head.next       # 要被反轉箭頭的節點 (一開始是 1)

        while nxt:
            save = nxt.next   # 存下下個 (一開始是 2)
            nxt.next = curr   # 改後面節點的箭頭: 1 -> 0
            curr = nxt        # 往前一步
            nxt = save

        head.next = None      # 原本的頭還指著 1,要手動斷開,不然有環
        return curr
        