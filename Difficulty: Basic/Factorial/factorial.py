#User function Template for python3


class Solution:
    def factorial (self, n):
        # code here
        if n<=1:
            return 1
        return n*self.factorial(n-1)