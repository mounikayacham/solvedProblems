class Node:
    def _init__(self,data):
        self.prev=None
        self.next=None
        self.data=data
class Deque:
    def __init__(self):
        self.front=None
        self.rear=None
        self.size=0
    def insert_front(self,data):
        new=Node(data)
        if self.front is None:
            self.front=self.rear=new
            return
        new.next=self.front
        self.front.prev=new
        self.front=new
        self.size+=1
    def insert_rear(self,data):
        new=Node(data)
        if self.front is None:
            self.front=self.rear=new
        else:
            self.rear.next=new
            new.prev=self.rear
            self.rear=new
            self.size+=1
    def delete_front(self):
        if self.front is None:
            return f'error : queue is empty'
        else:
            t=self.front
            self.front=self.front.next
            if self.front:
                self.front.prev=None
            else:
                self.rear=None
            del t
            self.size-=1
    def delete_rear(self):
        if self.front is None:
            return f'error : queue is empty'
        else:
            t=self.rear
            self.rear=self.rear.prev
            if self.rear:
                self.rear.next=None
            else:
                self.front=None
            del t
            self.size-=1
    def get_front(self):
        return -1 if self.front is None else self.front.data
    def get_rear(self):
        return -1 if self.front is None else self.rear.data

dq = Deque()
dq.insert_rear(5)
dq.insert_rear(10)
print("Rear:", dq.get_rear())
dq.delete_rear()
print("New Rear:", dq.get_rear())

dq.insert_front(15)
print("Front:", dq.get_front())
print("Size:", dq.get_size())

dq.delete_front()
print("New Front:", dq.get_front())


















        
        
