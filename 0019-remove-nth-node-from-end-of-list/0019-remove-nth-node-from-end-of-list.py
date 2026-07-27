# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        l=0
        curr=head

        while curr:
            curr=curr.next
            l+=1
        
        if n==l:
            return head.next
        
        curr=head
        s=l-n-1

        for i in range(s):
            curr=curr.next
        
        curr.next=curr.next.next
        return head     