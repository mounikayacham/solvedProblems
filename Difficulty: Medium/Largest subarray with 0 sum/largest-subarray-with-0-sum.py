class Solution:
    def maxLen(self, arr):
        #code here
        h={}
        s=0
        Max=0
        for i in range(len(arr)):
            s+=arr[i]
            if s==0:
               Max=i+1
            if s in h:
                Max=max(Max,i-h[s])
            else:
                h[s]=i
        return Max
        