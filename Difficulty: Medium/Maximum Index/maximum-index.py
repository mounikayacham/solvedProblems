class Solution:
    def maxIndexDiff(self, arr):
        # code here
        n=len(arr)
        p=[0]*n
        p[0]=arr[0]
        for i in range(1,n):
           p[i]=min(p[i-1],arr[i])
        s=[0]*n
        s[n-1]=arr[n-1]
        for j in range(n-2,-1,-1):
            s[j]=max(s[j+1],arr[j])
        i=0
        j=0
        m=-1
        while i<n and j<n:
            if p[i]<=s[j]:
                m=max(m,j-i)
                j+=1
            else:
                i+=1
        return m
            
         