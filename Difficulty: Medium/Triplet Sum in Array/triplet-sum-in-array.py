#User function Template for python3
class Solution:
    # Function to find if there exists a triplet in the array arr[] which sums up to target.
    def hasTripletSum(self, arr, target):
        # Your Code Here
        arr.sort()
        n=len(arr)
        for i in range(n-2):
            left=i+1
            right=n-1
            while left<right:
                t=arr[i]+arr[left]+arr[right]
                if t==target:
                    return True
                elif t>target:
                    right-=1
                else:
                    left+=1
        return False