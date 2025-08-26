class MyStack:


    # class StackNode:

    # # Constructor to initialize a node
    # def __init__(self, data):
    #     self.data = data
    #     self.next = None
        
    #Function to push an integer into the stack.
    def __init__(self):
        self.top=None
    def push(self, data):
        new=StackNode(data)
        new.next=self.top
        self.top=new
        

        # Add code here


    #Function to remove an item from top of the stack.
    def pop(self):
        # Add code here
        if self.top is None:
            return -1
        poped=self.top.data
        self.top=self.top.next
        return poped