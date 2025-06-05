class Solution:
    def addBinary(self, a: str, b: str) -> str:
        D=int(a,2)
        D1=int(b,2)
        c=D+D1
        res=bin(c)
        print(res[2:])
        return res[2:]
        