"""index is the node which is to be displayed in output
  Node is defined as
class Node:
    def __init__(self, data):
		self.data = data
		self.next = None
# Linked List class contains a Node object
class LinkedList:
    def __init__(self):
        self.head = None
This is method only submission.
 You only need to complete below method.
"""
class Solution:
    def GetNth(self, head, index):
        # Code Here
        if head is None:
            return -1
        t=head
        p=1
        while t and p<index:
            p+=1
            t=t.next
        if t:
            return t.data
        return -1
        