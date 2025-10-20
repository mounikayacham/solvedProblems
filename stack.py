class stack:
    def __init__(self):
        self.stack=[]
    def push(self,data):
        self.data=data
        self.stack.append(self.data)
    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        else:
            return "Underflow We can't pop the element"
        
    def peek(self):
        if self.is_empty():
            return self.stack[-1]
        else:
            return "Overflow Queue is empty"
    def is_empty(self):
        return len(self.stack)==0
    def print(self):
        if self.is_empty():
            return "We can't print the stack because Stack is empty"
        #bottom to top
        '''for i in range(len(self.stack)):
            print(self.stack[i],end=' ')'''
        #top to bottom
        return self.stack[::-1]
obj=stack()
print(obj.print())
obj.push(56)
obj.push(9)
obj.push(78)
obj.push(67)
obj.push(47)
print(obj.peek())
print(obj.is_empty())
print(obj.pop())
print(obj.print())
