class Solution:
    # Function to find triplets with zero sum.
    def findTriplets(self, arr):
        #code here
        arr.sort()
        n=len(arr)
        for i in range(n-2):
            left=i+1
            right=n-1
            while left<right:
                t=arr[left]+arr[i]+arr[right]
                if t==0:
                    return True
                elif t<0:
                    left+=1
                else:
                    right-=1
        return False