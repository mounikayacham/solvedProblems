
class Solution:
    def isBalanced(self, s):
        # code here
        m={')':'(','}':'{',']':'['}
        stack=[]
        for char in s:
            if char in m.values():
                stack.append(char)
            elif char in m:
                if not stack or stack[-1]!=m[char]:
                    return False
                stack.pop()
            else:
                pass
        return not stack
        