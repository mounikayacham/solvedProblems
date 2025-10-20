class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class stack:
    def __init__(self):
        self.top=None
    def push(self,data):
        new=Node(data)
        new.next=self.top
        self.top=new
    def pop(self):
        if self.is_empty():
            return f'Stack is empty'
        popped=self.top
        self.top=self.top.next
        return popped.data
    def peek(self):
        if self.is_empty():
            return f'Stack is empty'
        return self.top.data
    def is_empty(self):
        if self.top is None:
            return True
        return False
    def display(self):
        cur=self.top
        if cur is None:
            print('Stack is empty')
            return
        #print('stack from top')
        res='stack from top'
        while cur:
            #print(cur.data)
            res+='\n'+str(cur.data)
            cur=cur.next
        return res
st=stack()
st.push(23)
st.push(3)
st.push(4)
st.push(29)
st.push(93)
st.push(43)
st.push(57)
st.push(67)
print(st.display())
print(st.is_empty())
print(st.pop())
print(st.peek())
'''arr=list(map(int,input().split()))
def next_greater(arr):
    s=[]
    res=[-1]*(len(arr))
    for i in range(len(arr)):
        while s and arr[i]>arr[s[-1]]:#while s and arr[i]<arr[s[-1]]:
            idx=s.pop()
            res[idx]=arr[i]
        s.append(i)
    return res
print(next_greater(arr))
'''
'''def precedence(op):
    if op=='+' or op=='-':
        return 1
    elif op=='*' or op=='/':
        return 2
def infix_to_postfix(ex):
    s=[]
    res=''
    for ch in ex:
        if ch.isalnum():
            res+=ch
        elif ch=='(':
            s.append(ch)
        elif ch==')':
            while s and s[-1]!='(':
                res+=s.pop()
            s.pop()
        else:
            while s and precedence(ch)<=precedence(s[-1]):
                res+=s.pop()
            s.append(ch)
    while s:
        res+=s.pop()
    return res
print(infix_to_postfix('a-b+c*b'))                
'''
