# your task is to complete this function
# function should return new head pointer

'''
class node:
    def __init__(self):
        self.data = None
        self.next = None
'''

def deleteNode(head, x):
    # Code here
    if x==1:
        return head.next
    c=1
    t=head
    while t is not None and c<x-1:
        c+=1
        t=t.next
    if t is not None and  t.next is not None:
        t.next=t.next.next
    return head
    
            