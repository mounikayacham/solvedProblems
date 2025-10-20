class Node:
    def __init__(self,value):
        self.next=None
        self.value=value
class Linkedlist:
    def __init__(self):
        self.head=None
    def insertEnd(self,value):
        new=Node(value)
        if self.head is None:
            self.head=new
            return
        t=self.head
        while t.next:
            t=t.next
        t.next=new
    def insertatBegin(self,value):
        new=Node(value)
        '''if self.head is None:
            self.head=new
            return''' # There is no need of checking the head 
        new.next=self.head
        self.head=new
    '''def insertpos(self,value,pos):
        new=Node(value)
        if pos<0:
            return
        if pos==1:
            new.next=self.head
            self.head=new
            return
        p=1
        t=self.head
        while t and p<pos-1:
            t=t.next
            p=p+1
        if not t:
            return
        new.next=t.next
        t.next=new'''
    def insertpos(self,val,pos):
        new=Node(val)
        if pos==0:
            new.next=self.head
            self.head=new
            return
        t=self.head
        for i in range(pos-1):
            t=t.next
        new.next=t.next
        t.next=new
    def deleteFront(self):
        if self.head is None:
            return 'error'
        if self.head.next is None:
            self.head=None
            return 'Element was deleted'
        k=self.head.value
        self.head=self.head.next
        return f'Front Element {k} is deleted'
    def deleteEnd(self):
        if self.head is None:
            return 'error'
        if self.head.next is None:
            self.head=None
            return 'Element was deleted'
        t=self.head
        while t.next.next:
            t=t.next
        k=t.next.value
        t.next=None
        return f'last element {k} was deleted'
    def deletepos(self,pos):
        if  not self.head:
            return 'error'
        if pos==0:
            self.head=self.head.next
            return f'element is deleted'
        t=self.head
        p=0
        while t.next.next and p<pos-1:
            t=t.next
            p=p+1
        if not t.next:
            return 'out of range'
        k=t.next.value
        t.next=t.next.next
        return f'Node {k} is deleted'
    def display(self):
        if self.head is None:
            print('error')
            return 
        t=self.head
        while t:
            print(t.value,end='-->')
            t=t.next
        print("None")
      
k=Linkedlist()
k.insertEnd(9)
k.insertEnd(5)
k.insertEnd(6)
k.insertpos(4,3)
k.insertpos(5,2)
k.insertatBegin(8)
k.display()
print(k.deleteFront())
print(k.deleteEnd())
print(k.deletepos(2))
print(k.deletepos(8))

arr=[4,6,7,8,9,10]
p=Linkedlist()
for i in arr:
    p.insertEnd(i)
p.display()
            
'''class Node:
    def __init__(self,value=0,next=None):
        self.value=value
        self.next=next
        print(self.value)
class Linkedlist:
    def __init__(self,value=0):
        self.head=None
Node(5)
Node(7)
Node(8)
'''










        
