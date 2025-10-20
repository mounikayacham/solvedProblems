class stack:
    def __init__(self):
        self.stack=[]
        self.minstack=[]
    def push(self,x):
        self.stack.append(x)
        if not self.minstack or x<=self.minstack[-1]:
            self.minstack.append(x)
        #if not self.minstack or x>=self.minstack[-1]: this condition is for the max stackself.minstack.append(x)
    def pop(self):
        if not self.stack:
            print("Stack is underflowing")
            return
        top=self.stack.pop()
        if top==self.minstack[-1]:
            self.minstack.pop()
            return top
    def get_top(self):
        if not self.stack:
            print("Stack is empty")
            return
        return self.stack[-1]
    def get_min(self):
        if not self.minstack:
            print("Stack is empty")
            return
        return self.minstack[-1]
    
j=stack()
j.push(45)
j.push(56)
j.push(98)
j.push(23)
j.push(67)
j.push(90)
print(j.get_top())
print(j.get_min())
