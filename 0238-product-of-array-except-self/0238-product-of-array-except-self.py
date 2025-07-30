class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        '''n=len(nums)
        res=[]
        for i in range(len(num)):
            pre=nums[n-1]
            k=n-i-1
            pre*=nums[k]
            res.append(pre)
        return res
        '''
        n=len(nums)
        k=[1]*n
        pre=1
        for i in range(n):
            k[i]=pre
            pre*=nums[i]
        suf=1
        for i in range(n-1,-1,-1):
            k[i]*=suf
            suf*=nums[i]
        return k



        