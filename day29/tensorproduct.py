from numpy import array
from numpy import tensordot

# define first vector
A=array([1,2])

# Define second vector
B=array([3,4])



# Calculate tensor product
C=tensordot(A,B, axes=0)
print(C)