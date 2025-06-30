#function Template for python3

"""
# Node Class

class Node:
    def __init__(self, val):
        self.data = val
        self.next = None

"""

class Solution:
    def reverseList(self, head):
        # Code here
        prev=None
        c=head
        while c:
            new=c.next
            c.next=prev
            prev=c
            c=new
        return prev
            
            