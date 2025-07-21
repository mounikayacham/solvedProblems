#User function Template for python3

class Solution:
    def removeConsecutiveCharacter(self, s):
        # code her
        res=s[0]
        if not s:
           return s
        for i in range(1,len(s)):
            if s[i]!=s[i-1]:
                res+=s[i]
        return res