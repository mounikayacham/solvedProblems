class Solution:
    def findUnion(self, a, b):
        # code here 
        i=0
        j=0
        n,m=len(a),len(b)
        res=[]
        while i<n and j<m:
            if i>0 and a[i]==a[i-1]:
                i+=1
                continue
            if j>0 and b[j]==b[j-1]:
                j+=1
                continue
            if a[i]<b[j]:
                res.append(a[i])
                i+=1
            elif a[i]>b[j]:
                res.append(b[j])
                j+=1
            else:
                res.append(a[i])
                i+=1
                j+=1
        while i<n:
            if i==0 or a[i]!=a[i-1]:
                res.append(a[i])
            i+=1
        while j<m:
            if j==0 or b[j]!=b[j-1]:
                res.append(b[j])
            j+=1
        return res
            
            