# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next or not head.next.next :
            return head
        
        oddp = current = head
        evenp = evenhead = head.next
        i = 1

        
        while current:
            if i >2 and i % 2 != 0:
                oddp.next = current
                oddp = oddp.next
            elif i>2 and i % 2 == 0:
                evenp.next = current 
                evenp = evenp.next
            i += 1
            current = current.next
        evenp.next = None
        oddp.next = evenhead

        return head             

        