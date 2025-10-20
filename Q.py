class Queue:
    def __init__(self):
        self.q=[]
    def insert(self,x):
        self.q.append(x)
    def delete(self):
        if self.is_empty():
            return "Error"
        k=self.q.pop(0)
        return k
    def is_empty(self):
        return  not self.q
    def peek(self):
        if self.is_empty():
            return "Error"
        p=self.q[0]
        return p
p=Queue()
p.insert(67)
p.insert(7)
p.insert(45)
p.insert(56)
print(p.delete())
print(p.delete())
print(p.q)
print(p.peek())



