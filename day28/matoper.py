from numpy import array
from numpy.linalg import inv
from numpy import trace
A=array([[1,2,3], [3,4,6], [5,6,7]])

print(A)
# transpose operation
# C=A.T

# print(C)

# inverse operation
# A=array([[1.0, 2.0], [3.0, 4.0]])

# print(A)
# # invert matrix
# B=inv(A) 
# print(B)

# # multiply A and B
# I=A.dot(B)
# print(I)
# Calculate trace

B=trace(A)
print(B)