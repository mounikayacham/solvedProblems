class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class Queue:
    def __init__(self):
        self.head=None
    def insert(self,data):
        new=Node(data)
        if self.head is None:
            self.head=new
            return
        cur=self.head
        while cur.next:
            cur=cur.next
        cur.next=new
    def display(self):
        if self.is_empty():
            return f'Queue is empty'
        cur=self.head
        res='Queue elements'
        while cur:
            res+='\n'+str(cur.data)
            cur=cur.next
        return res
    def delete(self):
        if self.is_empty():
            return f'Queue is empty'
        if self.head.next is None:
            return 'Only one element'
        cur=self.head
        while cur.next.next:
            cur=cur.next
        res=cur.next.data
        cur=cur.next
        return res
    def is_empty(self):
        return self.head is None
q=Queue()
q.insert(56)
q.insert(32)
q.insert(12)
q.insert(87)
q.insert(9)
q.insert(39)
print(q.display())
print('Deleted elemnet: ',q.delete())

        
