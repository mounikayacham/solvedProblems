class Solution:
    def nextLargerElement(self, arr):
        # code here
        res=[-1]*(len(arr))
        stack=[]
        for i in range(len(arr)-1,-1,-1):
            while stack and stack[-1]<=arr[i]:
                stack.pop()
            if stack:
                res[i]=stack[-1]
            stack.append(arr[i])
        return res