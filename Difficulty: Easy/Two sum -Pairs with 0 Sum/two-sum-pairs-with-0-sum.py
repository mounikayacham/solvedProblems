#User function Template for python3

class Solution:
    def getPairs(self, arr):
        # code here
        arr.sort()
        k=[]
        seen=set()
        i=0
        j=len(arr)-1
        while(i<j):
            if arr[i]+arr[j]==0:
                if (arr[i],arr[j]) not in seen:
                    k.append([arr[i],arr[j]])
                seen.add((arr[i],arr[j]))
                i+=1
                j-=1
            elif (arr[i]+arr[j])>0:
                j-=1
            else:
                i+=1
        return  k
                