'''stack=[]
stack.append("welcome Reethika")
stack.append("You are")
stack.append("Good")
print(stack)
print(stack.pop())
print(stack)
stack.append("Bad")
print(stack)

from collections import deque
stack=deque()
stack.append("welcome")
stack.append('To')
stack.append('Reethika')
stack.append('You are good')
stack.insert(10,20)
print(stack)'''
from queue import LifoQueue
stack=LifoQueue(maxsize=3)
stack.put(5)
stack.put(4)
stack.put(3)
print(stack)
print(stack.qsize())
print(stack.full())
stack.get()
print(stack.full())
