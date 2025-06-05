class Solution:
    def isPalindrome(self, x: int) -> bool:
        r=0
        k=x
        while x>0:
            p=x%10
            r=r*10+p
            x=x//10
        return r==k
        