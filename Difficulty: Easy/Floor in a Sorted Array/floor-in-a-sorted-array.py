class Solution:
    #User function Template for python3
    
    #Complete this function
    def findFloor(self, arr, x):
        #Your code here
        Max=0
        for i in range(len(arr)):
            if arr[i]<=x:
                Max=arr[i]
                k=i
        n=Max
        
        for p in range(len(arr)-1,-1,-1):
            if arr[p]==n:
                return p
        return -1
                
        