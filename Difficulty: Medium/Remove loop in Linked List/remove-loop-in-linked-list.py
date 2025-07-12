'''
# node class:

class Node:
    def __init__(self,val):
        self.next=None
        self.data=val

'''

class Solution:
    #Function to remove a loop in the linked list.
    def removeLoop(self, head):
        # code here
        slow=fast=head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
            if slow==fast:
                break
        else:
            return 
        if slow==head:
            while fast.next!=head:
                fast=fast.next
            fast.next=None
            return
        slow=head
        while slow.next!=fast.next:
            slow=slow.next
            fast=fast.next
        fast.next=None
            