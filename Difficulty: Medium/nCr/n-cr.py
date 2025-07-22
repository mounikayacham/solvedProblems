class Solution:
    def nCr(self, n, r):
        # code here
        def fact(n):
            if n<=0:
                return 1
            return n*fact(n-1)
        ncr=fact(n)//(fact(n-r)*fact(r))
        return ncr
        
    