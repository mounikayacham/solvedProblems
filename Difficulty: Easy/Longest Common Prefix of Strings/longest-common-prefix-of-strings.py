#User function Template for python3
class Solution:
    def longestCommonPrefix(self, arr):
        # code here
        pre=''
        for i in zip(*arr):
            if len(set(i))==1:
                pre+=i[0]
            else:
                break
        return pre
            