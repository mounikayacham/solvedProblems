class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        k=0
        s=[]
        s.append(k)
        for i in range(len(gain)):
            
            k+=gain[i]
            s.append(k)
        #print(s)
        
        '''for i in range(len(s)-1):
            if ((s[i]>0)and (s[i]<s[i+1])):
                return gain(i)
            else:
                return 0'''
        
        for j in range(len(s)):
            
            if s[j]<=s[j+1]:
                if s[i]>=0:
                    return s[i]
                else:
                    return 0



