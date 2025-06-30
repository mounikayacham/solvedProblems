#User function Template for python3

'''
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
'''
def displayList(head):
    #code here
    k=[]
    if head is None:
        return 
    t=head
    while t is not None:
        k.append(t.data)
        t=t.next
        
    return k
    