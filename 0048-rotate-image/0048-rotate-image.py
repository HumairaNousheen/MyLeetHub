class Solution(object):
    def rotate(self, matrix):
        n = len(matrix)

        # Step 1: transpose using upper triangle
        for i in range(n-1):
            for j in range(i+1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        # Step 2: reverse each row
        for row in matrix:
            row.reverse()

        return matrix
