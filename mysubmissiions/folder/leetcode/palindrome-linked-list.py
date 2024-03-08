# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        l1=[]
        while head:
            l1.append(head.val)
            head = head.next
        l,r=0,len(l1)-1
        while l<r:
            if l1[l] != l1[r]:
                return False
            l+=1
            r-=1    
        return True        


        