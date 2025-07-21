class Solution:
    def cntCoprime(self, arr):
       # code here
        def comMob(n,mu):
            is_prime=[1]*(n+1)
            mu[0]=0
            mu[1]=1
            for i in range(2,n+1):
                if is_prime[i]:
                    for j in range(i,n+1,i):
                        mu[j]*=-1
                        is_prime[j]=0
                    for j in range(i*i,n+1,i*i):
                        mu[j]=0
        def build(arr,freq):
            for x in arr:
                freq[x]+=1
        def computDivcnt(maxVal,freq,d):
            for i in range(1,maxVal+1):
                for j in range(i,maxVal+1,i):
                    d[i]+=freq[j]
        maxVal=max(arr)
        freq=[0]*(maxVal+1)
        d=[0]*(maxVal+1)
        mu=[1]*(maxVal+1)
        build(arr,freq)
        comMob(maxVal,mu)
        computDivcnt(maxVal,freq,d)
        res=0
        for k in range(1,maxVal+1):
            if mu[k]==0 or d[k]<2:
                continue 
            pairs=d[k]*(d[k]-1)//2
            res+=mu[k]*pairs
        return res
        """def gcd(a,b):
            if b==0:
                return a
            return gcd(b,a%b)
        n=len(arr)
        c=0
        for i in range(n-1):
            for j in range(i+1,n):
                if gcd(arr[i],arr[j])==1:
                    c+=1
        return c
            """
        