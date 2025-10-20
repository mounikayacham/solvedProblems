class Node:
    def __init__(self,val):
        self.val=val
        self.prev=None
        self.next=None
class Doubly:
    def __init__(self):
        self.head=None
    def insert(self,val):
        new=Node(val)
        if self.head is None:
            self.head=new
            return
        new.next=self.head
        self.head.prev=new
        self.head=new
    def insertend(self,val):
        new=Node(val)
        if self.head is None:
            self.head=new
            return
        t=self.head
        while t.next:
            t=t.next
        new.prev=t
        t.next=new
    def insertatpos(self,val,pos):
        new=Node(val)
        if pos==0:
            self.insert(val)
            return
        t=self.head
        p=1
        '''while t and p<pos:
            p+=1
            t=t.next'''
        for i in range(pos-1):
            if not t:
                print("Out of rangge")
                return
            t=t.next
        if t is None:
             return "Out of range"
        new.next=t.next
        new.prev=t
        if t.next:
            t.next.prev=new
        t.next=new
    def display(self):
        if self.head is None:
            return
        t=self.head
        while t:
            print(t.val,end="-->")
            t=t.next
        print("None")
    def delete_begin(self):
        if self.head is None:
            print("List is Empty")
            return
        if self.head.next is None:
            self.head=None
            return
        self.head=self.head.next
        self.head.prev=None
    def delete_end(self):
        if self.head is None:
            print("List is Empty")
            return
        if self.head.next is None:
            self.head=None
            return
        t=self.head
        '''while t.next.next:
            t=t.next
        t.next=None'''
        while t.next:
            t=t.next
        t.prev.next=None
    def delete_pos(self,pos):
        if self.head is None:
            return "Dll is empty"
        if pos==0:
            self.delete_begin()
            return
        '''temp=self.head
        while temp.next.next and c<pos-1:
            temp=temp.next
            c+=1
        if not temp.next and temp.prev:
            return "overloaded"
        temp.next.prev=temp
        temp.next=temp.next.next'''
        t=self.head
        for i in range(pos):
            if not t:
                return
            t=t.next
        if not t:
            return
        if  t.next:
            t.next.prev=t.prev
        
        if t.prev:
            t.prev.next=t.next
             

p=Doubly()
p.insert(8)
p.insertend(6)
p.insertatpos(4,2)
p.delete_pos(1)
p.display()
        
