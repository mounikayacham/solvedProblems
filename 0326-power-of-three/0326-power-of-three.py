class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        k=n**(1//3)
        if n<=0:
            return False
        if k==int(k):
            return True
        return False
        