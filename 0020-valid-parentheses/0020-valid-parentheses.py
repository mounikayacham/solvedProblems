class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        mapping={']':'[','}':'{',')':'('}
        for char in s:
            if char in mapping.values():
                stack.append(char)
            elif not stack or mapping[char]!=stack.pop():
                return False
        return True

        