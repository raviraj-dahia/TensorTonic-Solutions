import numpy as np

def matrix_transpose(A):
    """
    Return the transpose of matrix A (swap rows and columns).
    """
    matrix = np.array(A)# Write code here
    rows = matrix.shape[0]
    cols = matrix.shape[1]

    result = np.zeros((cols,rows))
   

    for i in range(rows):
        for j in range(cols):
             result[j][i] = matrix[i][j]
    return result      
            
