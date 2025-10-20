class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class Linkedlist:
    def __init__(self):
        self.head=None
        self.tail=None
    def addLast(self,data):
        new=Node(data)
        if self.head is None and self.tail is None:
            self.head=new
            self.tail=new
            return
        t=self.head
        while t.next:
            t=t.next
        t.next=new
    def addFirst(self,data):
        new=Node(data)
        if self.head==None and self.tail==None:
            self.head=new
            self.tail=new
            return
        new.next=self.head
        self.head=new
    def print(self):
        if self.head==None and self.tail==None:
            return
        t=self.head
        while t:
            print(t.data,end="-->")
            t=t.next
        print("None")
ll=Linkedlist()
ll.addFirst(1)
ll.addLast(2)
ll.addLast(3)
ll.addFirst(4)
ll.print()