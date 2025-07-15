class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        zerr=set()
        zerc=set()
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j]==0:
                    zerr.add(i)
                    zerc.add(j)
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if i in zerr  or j in zerc:
                    matrix[i][j]=0
        return matrix
        
        
        