class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        D=''
        for i in range(len(digits)):
            D+=str(digits[i])
        res=str(int(D)+1)
        k=[]
        for i in res:
            k.append(int(i))
        return k

        

        