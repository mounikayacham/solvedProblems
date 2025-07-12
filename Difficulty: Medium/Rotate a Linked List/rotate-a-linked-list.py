# Your task is to complete this function

'''

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

'''


class Solution:
    
    #Function to rotate a linked list.
    def rotate(self, head, k):
        # code here
        if not head or not head.next or k==0:
            return head
        t=head
        l=1
        while t.next:
            t=t.next
            l+=1
        k=k%l
        if k==0:
            return head
        s=l-k 
        cur=head
        for _ in range(k-1):
            cur=cur.next
        new=cur.next
        cur.next=None
        t.next=head
        return new
            