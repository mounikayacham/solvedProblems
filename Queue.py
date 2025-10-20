from collections import deque
class Queue:
    def __init__(self):
        self.queue=deque()
    def enque(self,data):
        self.data=data
        self.queue.append(self.data)
    def deque(self):
        if not self.is_empty():
            return  self.queue.popleft()
        else:
            return "Queue is emtpy"
    def is_empty(self):
        return len(self.queue)==0
    def print(self):
        if self.is_empty():
            return "We can't print the queue because queue is empty"
        for i in range(len(self.queue)):
                       print(self.queue[i],end=' ')

obj1=Queue()
print(obj1.is_empty())
obj1.enque(56)
obj1.enque(6)
obj1.enque(45)
obj1.enque(5)
obj1.enque(34)
obj1.enque(35)
obj1.print()
print()
print(obj1.deque())
obj1.print()

        
            
    
