class circularQueue:
    def __init__(self,size):
        self.maxsize=size
        self.front=-1
        self.rear=-1
        self.arr=[0]*self.maxsize
    def enQueue(self,val):
        if self.isEmpty():
            self.front=0
            self.rear=0
            self.arr[self.rear]=val
        else:
            self.rear=(self.rear+1)%self.maxsize
            if self.rear==self.front:
                print(" queue is full")
                self.rear=(self.rear-1+self.maxsize)%self.maxsize
            else:
                self.arr[self.rear]=val
    def deQueue(self):
        if  not self.isEmpty():
            val=self.arr[self.front]
            if self.front==self.rear:
                self.front=-1
                self.rear=-1
            else:
                self.front=(self.front+1)%self.maxsize
            return val
        else:
            print("empty")
    def isEmpty(self):
        return  self.front==-1 and self.rear==-1
    def peek(self):
        if self.isEmpty():
            print('empty')
        else:
            print(self.arr[self.front])
k=circularQueue(5)
k.enQueue(6)
k.enQueue(9)
k.enQueue(54)
k.enQueue(4)
k.enQueue(3)
print(k.deQueue())
print(k.isEmpty())
k.peek()








    
