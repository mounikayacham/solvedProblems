
#implementation of  the data structure
#1.Initialization
#2.Add / Remove
#3.Input / Output
#4.Traversal

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class Linkedlist:
    def __init__(self):
        self.head=None

        
    def insert_at_end(self,data):
        new=Node(data)
        if self.head is None:
            self.head=new
            return
        t=self.head
        while t.next:
            t=t.next
        t.next=new
    def insert_at_front(self,data):
        new=Node(data)
        if self.head is None:
            self.head=new
            return
        else:
            new.next=self.head
            self.head=new
            return
    def insert_at_position(self,pos,data):
        new=Node(data)
        if pos<0:
            return  'position is greater then the length'
                
        if pos==1:
            new.next=self.head
            self.head=new
            return
        c=1
        temp=self.head
        while c<pos-1 and temp:
            c+=1
            temp=temp.next
        if  not temp:
            return 
        new.next=temp.next
        temp.next=new


        
    def delete_at_front(self):
        if self.head is None:
            return "Linkedlist is empty"
        if self.head.next is None:
            self.head=None
            return "Element Deleted"
        self.head=self.head.next
        return "Front element Deleted"
    def delete_at_end(self):
        if self.head is None:
            return "lLinkedlist is empty"
        if self.head.next is None:
            self.head=None
            return "Element Deleted"
        temp=self.head
        while temp.next.next:
            temp=temp.next
        temp.next=None
        return "Last element is  Deleted"
    def delete_at_pos(self,pos):
        if self.head is None:
            return "Linkedlist is empty"
        if pos==1:
            self.head=self.head.next
            return " element Deleted"
        temp=self.head
        c=1
        while temp.next.next  and c<pos-1:
            c+=1
            temp=temp.next
        if not temp.next:
            return "position is greater then the length"
        temp.next=temp.next.next
        return 'element is deleted'
             
             
        
            
    def print(self):
        temp=self.head
        if temp is None:
            print("linked list is empty")
            return
        while temp:
            print(temp.data,end="->")
            temp=temp.next
        print()
        '''else:
            print("Liked list is empty")'''
    def length(self):
        c=0
        t=self.head
        while t:
            c+=1
            t=t.next
        return c

    '''def reverseList(self):
        prev = None
        curr = self.head
        
        while curr:
            next_node = curr.next   # store next node
            curr.next = prev        # reverse the pointer
            prev = curr             # move prev forward
            curr = next_node        # move curr forward
            print(prev,end=' ')  '''
obj=Linkedlist()
l=[1,2,3,4,5,5,6]
for i in l:
    obj.insert_at_end(i)
obj.insert_at_end(34)
obj.insert_at_end(45)
obj.insert_at_end(67)
obj.insert_at_end(78)
obj.insert_at_front(90)
obj.insert_at_position(2,52)
obj.print()
print(obj.delete_at_end())
obj.print()
print(obj.delete_at_front())
obj.print()
print(obj.delete_at_pos(2))
obj.print()
print(obj.delete_at_pos(6))

obj1=Linkedlist()
print(obj1.delete_at_end())
obj1.print()
print(obj1.delete_at_front())
obj1.print()
print(obj1.delete_at_pos(2))
obj1.print()
#print(obj1.reverseList())


        
