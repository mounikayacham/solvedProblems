class Solution:
    def rowWithMax1s(self, arr):
        # code here
        maxr=-1
        max1=0
        n=len(arr)
        m=len(arr[0])
        for i in range(n):
            low=0
            high=m-1
            while low<=high:
                mid=(low+high)//2
                if arr[i][mid]==1:
                   high =mid-1
                else:
                    low=mid+1
            n1=m-low
            if n1>max1:
                max1=n1
                maxr=i
        return maxr