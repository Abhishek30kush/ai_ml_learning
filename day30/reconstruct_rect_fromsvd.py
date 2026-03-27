# reconstruct rectangular matrix from svd
from numpy import array
from scipy.linalg import svd
from numpy import diag
from numpy import zeros

# Define a matrix
A=array([[1, 2], [3, 4], [5, 6]])
print(A)
# factorize
U, s, V= svd(A)
print(U)
print(s)
print(V)
# create m*n sigma matrix
Sigma=zeros((A.shape[0], A.shape[1]))
# poipulate sigma with n*n diagnal matrix
Sigma[:A.shape[1], :A.shape[1]] = diag(s)
# reconstruct matrix
B=U.dot(Sigma.dot(V))
print(B)