# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        priv,current = None ,head
        while current:
            nex=current.next
            current.next = priv
            priv=current
            current = nex
        return priv     
        