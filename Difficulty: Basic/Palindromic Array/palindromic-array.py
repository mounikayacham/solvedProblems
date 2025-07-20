# Your task is to complete this function
# Function should return true/false
def isPalinArray(arr):
    # Code here
    for i in range(len(arr)):
        n=arr[i]
        r=0
        k=arr[i]
        while n>0:
            p=n%10
            r=r*10+p
            n=n//10
        if k!=r:
            return False
    return True