'''
# Node Class:
class Node:
    def _init_(self,val):
        self.data = val
        self.left = None
        self.right = None
'''
class Solution:
#Function to return a list containing the preorder traversal of the tree.
    def preorder(self,root):
        
        res=[]
        def helper(root):
            if root is None:
                return []
            res.append(root.data)
            helper(root.left)
            helper(root.right)
        helper(root)
        return res
   
    # code here