class Solution:
    def search(self, pat, txt):
        # code here
        res=[]
        for i in range(len(txt)-len(pat)+1):
            if txt[i:i+len(pat)]==pat:
                res.append(i)
        return res