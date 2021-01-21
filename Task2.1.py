# sparse matrix using csc_matrix()

# Import required package
import numpy as np
from scipy.sparse import csc_matrix
# row stores the row position of non zero values
row = np.array([0, 0, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6, 7, 7, 7, 8, 8, 9, 9])
# col stores the column position of non zero values
col = np.array([0, 2, 1, 3, 0, 2, 4, 1, 3, 5, 2, 4, 6, 3, 5, 7, 4, 6, 8, 5, 7, 9, 6, 8, 7, 9])

# data stores the non zero values in the matrix
data = np.array([2, 1, 2, 1, 1, 2, 1, 1, 2, 1, 1, 2, 1, 1, 2, 1, 1, 2, 1, 1, 2, 1, 1, 2, 1, 2], dtype=float)

# creating sparse matrix
sparseMatrix = csc_matrix((data, (row, col)), shape=(10, 10)).toarray()
# print the sparse matrix
print(sparseMatrix)