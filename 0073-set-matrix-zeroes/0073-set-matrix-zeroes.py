class Solution(object):
    def setZeroes(self, matrix):
        if not matrix:
            return
        
        col_var = 1
        row = len(matrix) #4
        col = len(matrix[0]) #4

        # Marking all the boxes
        for i in range(row):
            if matrix[i][0] == 0:
                col_var = 0  # Mark first column should be zero
            for j in range(1, col):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0

        # Step 1: Set matrix elements to zero based on markings
        for i in range(row-1 , 0, -1): #3,2,1
            for j in range(col-1, 0, -1):  # 3,2,1
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

        # Step 2: Handle the first row separately
        if matrix[0][0] == 0:
            for j in range(col):
                matrix[0][j] = 0

        # Step 3: Handle the first column separately
        if col_var == 0:
            for i in range(row):
                matrix[i][0] = 0

        

        
        
        