from collections import Counter
class Solution:
    def frequencyCount(self, arr):
        #  code here
        res=[]
        fre=Counter(arr)
        n=len(arr)
        for i in range(1,n+1):
            res.append(fre.get(i,0))
        return res
            