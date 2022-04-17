# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head == None:
            return False
        itr = ListNode(head.val, head.next)
        arr = []
        while itr:
            if itr in arr:
                return True
            arr.append(itr)
            itr = itr.next
        return False
    def hasCycleHashSet(self, head: Optional[ListNode]) -> bool:
        if head == None:
            return False
        hashSet = {}
        count = 0
        itr = ListNode(head.val, head.next)
        while itr:
            if itr in hashSet.values():
                return True
            hashSet[count] = itr
            itr = itr.next
            count += 1
        return False