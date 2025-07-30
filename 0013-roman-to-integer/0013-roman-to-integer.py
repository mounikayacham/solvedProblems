class Solution:
    def romanToInt(self, s: str) -> int:
        r={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        t=0
        pre=0
        for v in reversed(s):
            val=r[v]
            if val<pre:
                t-=val
            else:
                t+=val
            pre=val
        return t

        