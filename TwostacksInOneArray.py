class stack:
    def __init__(self,n):
        self.size=n
        self.arr=[None]*n
        self.top1=-1
        self.top2=n
    def push1(self,x):
        if self.top1+1<self.top2:
            self.top1+=1
            self.arr[self.top1]=x
        else:
            print(f"Stack is overflow at stack1 By pushing : {x}")
    def push2(self,x):
        if self.top1+1<self.top2:
            self.top2-=1
            self.arr[self.top2]=x
        else:
            print(f"Stack is overflow at stack 2 By pushing: {x}")
    def pop1(self):
        if self.top1>=0:
            x=self.arr[self.top1]
            self.arr[self.top1]=None
            self.top1-=1
            return x
        else:
            return f"stack is underflow"
    def pop2(self):
        if self.top2<n:
            x=self.arr[self.top2]
            self.arr[self.top2]=None
            self.top2+=1
            return x
        else:
            return f"Stack is underflow"
    def display(self):
        print(self.arr)
k=stack(10)
k.push1(23)
k.push1(89)
k.push1(67)
k.push1(12)
k.push1(45)
k.push2(35)
k.push2(73)
k.push2(78)
k.push2(89)
k.display()
k.push2(32)
k.push2(56)
k.display()
k.push1(96)   
            
            
        
