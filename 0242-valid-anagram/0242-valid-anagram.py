class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        fre={}
        for i in s:
            fre[i]=fre.get(i,0)+1
        for i in t:
            fre[i]=fre.get(i,0)-1
        for i in fre.values():
            if i!=0:
                return False
        return True

        