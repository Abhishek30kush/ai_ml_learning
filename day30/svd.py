# singular value decomoposition 
from numpy import array
from scipy.linalg import svd

# Define a matrix
A=array([[1, 2], [3, 4], [5, 6]])
print(A)
# factorize
U, s, V= svd(A)
print(U)
print(s)
print(V)
