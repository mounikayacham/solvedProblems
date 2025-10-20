from collections import deque
class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
class Tree:
    def __init__(self):
        self.root=None
    
def Bst(root):
    if not root:
        return []
    res=[]
    q=deque([root])
    while q:
        level=[]
        for i in range(len(q)):
            node=q.popleft()
            level.append(node)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        res.append(level)
    return res

root=Node(3)
root.left=Node(1)
root.right=Node(7)
root.left.left=Node(3)
root.left.right=Node(8)
root.left.right.left=Node(2)
root.left.left.right=Node(9)
print(Bst(root))