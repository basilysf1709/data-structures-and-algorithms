# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head.next:
            return None
        temp = ListNode(0, head)
        lp = ListNode(temp.val, temp.next)
        rp =  ListNode(temp.val, temp.next)
        count = 0
        while rp:
            if count > n:
                lp = lp.next
            rp = rp.next
            count += 1
        if n == count - 1:
            return head.next
        lp.next = lp.next.next
        return temp.next
