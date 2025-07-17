#User function Template for python3


class Solution:
    #Function to check if a string can be obtained by rotating
    #another string by exactly 2 places.
    def isRotated(self,s1,s2):
        #code here
        if len(s1)!=len(s2):
            return False
        n=len(s1)
        cl=True
        an=True
        for i in range(n):
            if (s1[i]!=s2[(i+2)%n]):
                cl=False
                break
        for j in range(n):
            if (s1[(j+2)%n]!=s2[j]):
                an=False
                break
        return cl or an