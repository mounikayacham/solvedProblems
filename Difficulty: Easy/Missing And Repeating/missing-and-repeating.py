class Solution:
    def findTwoElement(self, arr):
        # code here
        arr.sort()
        res=[]
        for i in range(1,len(arr)):
            if arr[i]==arr[i-1]:
                res.append(arr[i])
                break
        s=set(arr)
        for i in range(1,len(arr)+1):
            if i not in s:
                res.append(i)
                break
                
        return res

