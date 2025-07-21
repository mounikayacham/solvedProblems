"""Node is defined as

class Node:
    def __init__(self, data):
		self.data = data
		self.next = None
"""
class Solution:
    def reverseKGroup(self, head, k):
        # Code here
        if head is None or k==1:
            return head
        prev = None
        cur = head
        count = 0

        # Count actual nodes to reverse in this group
        t = head
        while t and count<k:
            t=t.next
            count+=1
        for _ in range(count):
            next_new=cur.next
            cur.next=prev
            prev=cur
            cur=next_new
        if next_new:
            head.next=self.reverseKGroup(next_new,k)
        return prev
     