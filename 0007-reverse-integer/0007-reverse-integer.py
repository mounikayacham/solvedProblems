class Solution:
    def reverse(self, x: int) -> int:
        r=0
        k=x
        x=abs(x)
        if k<(-2**32) or k>(2**32):
            return 0
        while x>0:
            p=x%10
            r=r*10+p
            x=x//10
        if k<0:
            return 0-r
        return r
        