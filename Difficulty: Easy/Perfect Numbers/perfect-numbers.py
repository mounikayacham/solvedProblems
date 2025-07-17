import math
class Solution:
    def isPerfect(self, n):
        # code here
        if n<=0:
            return False
        s=1
        for i in range(2,int(math.sqrt(n))+1):
            if n%i==0:
                s+=i
                if i!=n//i:
                    s+=n//i
        return s==n