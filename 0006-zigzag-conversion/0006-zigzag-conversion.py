class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows==1 or numRows>=len(s):
            return s
        row=['']*numRows
        i,step=0,1
        for ch in s:
            row[i]+=ch
            if i==0:
                step=1
            elif i==numRows-1:
                step=-1
            i+=step
        return ''.join(row)
        
        