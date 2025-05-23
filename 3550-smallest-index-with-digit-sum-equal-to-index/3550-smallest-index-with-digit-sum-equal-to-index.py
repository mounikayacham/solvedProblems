class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        k=[]
        for i in range(len(nums)):
            n=nums[i]
            s=0
            while n>0:
                p=n%10
                s+=p
                n=n//10
            if i==s:
                k.append(i)
        k.sort()
        if k:
            return k[0]
        else:
            return -1