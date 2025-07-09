
class Solution:
    def isBalanced(self, s):
        # code here
        mapping={')':'(','}':'{',']':'['}
        stack=[]
        for char in s:
            if char in mapping.values():
                stack.append(char)
            elif not stack or mapping[char]!=stack.pop():
                return False
        return  not stack