'''

	{
		# Node Class
		class Node:
		    def __init__(self, data):   # data -> value stored in node
		        self.data = data
		        self.next = None
	}

'''
#Function to check whether the list is palindrome.
class Solution:
    def isPalindrome(self, head):
        if not head or not head.next:
            return True
        #code here
        fast=slow=head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        prev=None
        cur=slow
        while cur:
            next=cur.next
            cur.next=prev
            prev=cur
            cur=next
        first=head
        sec=prev
        while sec:
            if first.data!=sec.data:
                return False
            first=first.next
            sec=sec.next
        return True
        
        