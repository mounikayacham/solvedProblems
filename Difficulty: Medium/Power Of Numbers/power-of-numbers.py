class Solution:
    def reverse_exponentiation(self, n):
        # code here
        a=n
        r=0
        while n>0:
            k=n%10
            r=r*10+k
            n=n//10
        return a**r