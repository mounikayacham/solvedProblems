class Solution:
    def transpose(self, mat):
        # Transpose of matrix
        m = []
        for i in range(len(mat[0])):         # columns -> rows
            k = []
            for j in range(len(mat)):        # rows -> columns
                k.append(mat[j][i])
            m.append(k)
        return m

        