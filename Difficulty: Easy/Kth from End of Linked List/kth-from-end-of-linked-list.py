'''
	A linked list node has the following structure
	{
		# Node Class
		class Node:
		    def __init__(self, data):   # data -> value stored in node
		        self.data = data
		        self.next = None
	}
'''
#Function to find the data of kth node from the end of a linked list
class Solution:
    def getKthFromLast(self, head, k):
        #code here
        t=head
        c=0
        while t:
            c+=1
            t=t.next
        if k>c:
            return -1
        l=head
        p=c-k
        C=0
        while C<p:
            l=l.next
            C+=1
        return l.data
       