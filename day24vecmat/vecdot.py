import numpy as np

print('B. Matrix Representation and Operations')

# Create a matrix
matrix = np.array([[1, 2], [3, 4]])

# Matrix multiplication
matrix_a = np.array([[1, 2], [3, 4]])
matrix_b = np.array([[5, 6], [7, 8]])
matrix_product = np.dot(matrix_a, matrix_b)
print(f"Matrix A:\n{matrix_a}")
print(f"Matrix B:\n{matrix_b}")
print(f"Matrix product of A and B:\n{matrix_product}")

# Transpose of a matrix
transpose = np.transpose(matrix)
print(f"Transpose of matrix:\n{transpose}")