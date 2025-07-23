class Solution:
    def subarraySum(self, arr):
        # code here 
        t=0
        n=len(arr)
        for i in range(n):
            t+=arr[i]*(i+1)*(n-i)
        return t
        