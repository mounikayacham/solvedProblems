# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if head is None or head.next is None:
            return True
        #find the middle
        slow=fast=head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        #reverse the second Half
        prev=None
        cur=slow
        while cur:
            nxt=cur.next
            cur.nxt=prev
            prev=cur
            cur=nxt
        sec=prev
        first=head
        #check the values
        while sec:
            if sec.val!=first.val:
                return False
            sec=sec.next
            first=first.next
        return True