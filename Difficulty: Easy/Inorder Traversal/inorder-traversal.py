'''
# Node Class:
class Node:
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right = None
'''

class Solution:
    def inOrder(self,root):
        # code her
        res=[]
        def helper(root):
            if not root:
                return []
            helper(root.left)
            res.append(root.data)
            helper(root.right)
        helper(root)
        return res