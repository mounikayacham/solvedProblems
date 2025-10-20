'''class Queue:
    def __init__(self):
        self.s1=[]
        self.s2=[]
    def enqueue(self,x):
        while self.s1:
            self.s2.append(self.s1.pop())
        self.s1.append(x)
        while self.s2:
            self.s1.append(self.s2.pop())
    def dequeue(self):
        if  not self.s1:
            print("Stack is empty you have to push the values to the :")
            return
        return self.s1.pop()
obj=Queue()
obj.enqueue(3)
obj.enqueue(5)
obj.enqueue(7)
obj.enqueue(9)
obj.enqueue(11)
print(obj.dequeue())
print(obj.dequeue())
print(obj.dequeue())
print(obj.dequeue())
print(obj.dequeue())'''


class Queue:
    def __init__(self):
        self.s1=[]
    def enqueue(self,x):
        self.s1.append(x)
    def dequeue(self):
        if not self.s1:
            print("Stack is empty you have to the elements to the stack")
        s=self.s1[-1]
        self.s1.pop()
        if not self.s1:
            return s
        item=self.dequeue()
        self.s1.append(s)
        return item
obj=Queue()
obj.enqueue(3)
obj.enqueue(5)
obj.enqueue(7)
obj.enqueue(9)
obj.enqueue(11)
print(obj.dequeue())
print(obj.dequeue())
print(obj.dequeue())
print(obj.dequeue())
print(obj.dequeue())













        
            
        
    
