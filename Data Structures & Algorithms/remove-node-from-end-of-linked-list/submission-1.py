# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # n_from_start = Lenth - n + 1
        l = head
        r = head
        for _ in range(n):
            r = r.next
        
        if not r:
            return head.next

        while r.next:
            l = l.next
            r = r.next
        
        temp = l.next
        l.next = temp.next

        return head
        
        

        



        