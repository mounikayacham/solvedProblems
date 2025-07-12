'''
# Node Class
class Node:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None
'''
class Solution:
    # Function to find the length of a loop in the linked list.
    def countNodesInLoop(self, head):
        #code here
        if not head:
            return 0
        fast=slow=head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
            c=1
            if slow==fast:
                t=slow.next
                while t!=slow:
                    c+=1
                    t=t.next
                return c
        return 0
            
                