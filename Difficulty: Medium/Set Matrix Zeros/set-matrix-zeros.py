class Solution:
    def setMatrixZeroes(self, mat):
        # code here
        set_r=set()
        set_c=set()
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j]==0:
                    set_r.add(i)
                    set_c.add(j)
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if i in set_r or j in set_c:
                    mat[i][j]=0
        return mat
        