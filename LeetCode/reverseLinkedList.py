# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prevNode, currNode = None, head
        while currNode != None:
            nxtNode = currNode.next
            currNode.next = prevNode
            prevNode = currNode
            currNode = nxtNode
        return prevNode

    # prevNode = None, currNode = head

    # while currNode:
    #     nxtNode = currNode.next
    #     currNode.next = prevNode
    #     prevNode = currNode
    #     currNode = nextNode
    # return prevNode
    # practice