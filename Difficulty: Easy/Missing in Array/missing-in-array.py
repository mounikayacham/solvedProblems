class Solution:
    def missingNum(self, arr):
        # code here
            n=len(arr)+1
            su=n*(n+1)//2
            e=sum(arr)
            return su-e