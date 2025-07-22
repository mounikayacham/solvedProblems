class Solution:
	def pythagoreanTriplet(self, arr):
	    # code here
	    '''n=len(arr)
    	arr=[x**2 for x in arr]
    	arr.sort()
    	for i in range(n-1,1,-1):
    	    t=arr[i]
    	    l=0
    	    r=i-1
    	    while l<r:
    	        s=arr[l]+arr[r]
    	        if s==t:
    	            return True
    	        elif s<t:
    	            l+=1
    	        else:
    	            r-=1
    	return False
    	'''
    
        s = set(x * x for x in arr)
        n = len(arr)
        for i in range(n):
            for j in range(i + 1, n):
                if arr[i] ** 2 + arr[j] ** 2 in s:
                    return True
        return False
