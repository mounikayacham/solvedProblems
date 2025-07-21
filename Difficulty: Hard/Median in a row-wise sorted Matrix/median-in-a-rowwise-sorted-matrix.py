#User function Template for python3
from bisect import bisect_right
class Solution:
    def median(self, mat):
        #code here
        n=len(mat)
        m=len(mat[0])
        low=min(row[0] for row in mat)
        high=max(row[-1] for row in mat)
        d=((n*m)+1)//2
        while low<high:
            mid=(low+high)//2
            c=sum(bisect_right(row,mid) for row in mat)
            if c<d:
                low=mid+1
            else:
                high=mid
        return low