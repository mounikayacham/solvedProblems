class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=''.join(char for char in s if char.isalnum())
        s=s.lower()
        low=0
        high=len(s)-1
        while low<high:
            if s[low]!=s[high]:
                return False
            low+=1
            high-=1
        return True
        