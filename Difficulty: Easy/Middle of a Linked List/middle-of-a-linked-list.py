# your task is to complete this function

'''
class node:
    def __init__(data):
        self.data = data
        self.next = None
'''
class Solution:
    #  Should return data of middle node. If linked list is empty, then  -1
    def getMiddle(self, head):
        # Code here
        # return the value stored in the middle node
        t=head
        c=0
        while t:
            t=t.next
            c+=1
        if c%2==0:
            m=(c//2+((c//2)+1))//2
        else:
            m=c//2
        k=head
        C=0
        while C<m:
            k=k.next
            C+=1
        return k.data
        