class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None
class Double:
    def __init__(self):
        self.head=None
    def insert_at_last(self,data):
        new=Node(data)
        if self.head is None:
            self.head=new
            self.head.prev=None
            self.head.next=None
            return
        t=self.head
        while t.next:
            t=t.next
        t.next=new
        new.prev=t
    def insert_at_front(self,data):
        new=Node(data)
        if self.head is None:
            self.head=new
            return
        self.head.prev=new
        new.next=self.head
        self.head=new
    def insert_at_pos(self,pos,data):
        new=Node(data)
        if pos<0:
            return "Invalid"
        if pos==1:
            self.head.prev=new
            new.next=self.head
            self.head=new
            return
        c=1
        temp=self.head
        while temp and c<pos-1:
            temp=temp.next
            c+=1
        if  not temp:
            return
        new.next=temp.next
        new.prev=temp
        temp.next=new
    def delete_at_front(self):
        if self.head is None:
            return "Doubly linked list is empty"
        if self.head.next is None:
            self.head=None
            return "Element is deleted"
        self.head.next.prev=None
        self.head=self.head.next
        return "element Deleted"
    
        
    def delete_at_end(self):
        if self.head is None:
            return "Doubly linked list is empty"
        if self.head.next is None:
            self.head=None
            return "Element is deleted"
        temp=self.head
        while temp.next.next:
            temp=temp.next
        #temp.next.prev=None  # it is not necessory for deleting element
        temp.next=None
        return "Last element Deleted"
    def delete_at_pos(self,pos):
        if self.head is None:
            return "Doubly linked list is empty"
        if self.head.next is None:
            self.head=None
            return "Element is deleted"
        c=1
        temp=self.head
        while temp.next.next and c<pos-1:
            temp=temp.next
            c+=1
        if not temp.next and temp.prev:
            return "overloaded"
        temp.next.prev=temp
        temp.next=temp.next.next
        
        return "Element deleted at position"
    def revers(self):
        if self.head is None:
            return "List is Empty"
        else:
            temp=self.head
            while temp.next is not None:
                temp=temp.next
            while temp is not None:
                print(temp.data,end=' ')
                temp=temp.prev
                
        
        
    def print(self):
        temp=self.head
        if temp is None:
            print('Empty')
        while temp:
            print(temp.data,end="<--> ")
            temp=temp.next
        print()

obj=Double()
obj.insert_at_last(90)
obj.insert_at_last(45)
obj.insert_at_last(23)
obj.insert_at_last(12)
obj.insert_at_last(9)
obj.insert_at_front(67)
obj.insert_at_pos(2,78)
obj.print()
print(obj.delete_at_end())
print(obj.delete_at_front())
obj.print()
print(obj.delete_at_pos(3))
obj.print()
obj.revers()
