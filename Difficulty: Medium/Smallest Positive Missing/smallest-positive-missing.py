class Solution:
    def missingNumber(self, arr):
        # code here
        arr.sort()
        k=[]
        for i in range(len(arr)):
            if arr[i]>0:
                k.append(arr[i])
        e=1
        for i in range(len(k)):
            if k[i]==k[i-1] and i>0:
                continue
            if k[i]==e:
                e+=1
            if k[i]>e:
                return e
        return e