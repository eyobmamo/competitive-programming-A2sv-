# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        less , greater = ListNode(), ListNode()
        ltail, rtail = less ,greater
        
        current = head
        while current:
            if current.val < x:
                ltail.next = current
                ltail = ltail.next
            else:
                rtail.next = current
                rtail = rtail.next
            current = current.next

        ltail.next = greater.next
        rtail.next = None
        return less.next            

        