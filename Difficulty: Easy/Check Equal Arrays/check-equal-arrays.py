class Solution:
    def checkEqual(self, a, b) -> bool:
        #code her
        a.sort()
        b.sort()
        if len(a)!=len(b):
            return False
        if sorted(a)==sorted(b):
            return True