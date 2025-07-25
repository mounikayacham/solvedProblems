class Solution:
    def maxCircularSum(self, arr):
        totalsum=arr[0]
        minsum=arr[0]
        maxsum=arr[0]
        Cmaxsum=0
        Cminsum=0
        for i in range(1,len(arr)):
            Cmaxsum=max(Cmaxsum+arr[i],arr[i])
            maxsum=max(maxsum,Cmaxsum)
            Cminsum=min(Cminsum+arr[i],arr[i])
            minsum=min(minsum,Cminsum)
            totalsum+=arr[i]
        normalsum=maxsum
        circularsum=totalsum-minsum
        if totalsum==minsum:
            return normalsum
        return max(normalsum, circularsum)
        #print(sol.circularSubarraySum(arr))    
        # code here