# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        tmp = head
        newList = None
        tail = None
        while tmp:
            if newList is None:
                newList = ListNode(tmp.val, None)
                tail = newList
            else:
                tail.next = ListNode()
                tail = tail.next
                tail.val = tmp.val
                tail.next = None
            tmp = tmp.next
        tmp1 = head
        newList1 = None
        tail = None
        while tmp1:
            if newList1 is None:
                newList1 = ListNode(tmp1.val, None)
                tail = newList1
            else:
                tail.next = ListNode()
                tail = tail.next
                tail.val = tmp1.val
                tail.next = None
            tmp1 = tmp1.next
        curr, prev = newList, None
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        count = 1
        tail = head
        length = 0
        while tail:
            tail = tail.next
            length += 1
        tail = head
        newList1 = newList1.next
        while count < length + 1:
            if count != 1:
                if count % 2 == 0:
                    tail.next = prev
                    prev = prev.next
                else:
                    tail.next = newList1
                    newList1 = newList1.next
                tail = tail.next
            count += 1
        tail.next = None
    
        