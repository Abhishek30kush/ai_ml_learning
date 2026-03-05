from numpy import array
# from numpy import tril
# from numpy import triu
from numpy import diag

from numpy import identity
from numpy.linalg import inv
Q=array([[1,0], [0,-1]])
print(Q)

# inverser equivalence
V=inv(Q)
print(Q.T)
print(V)

# Identity equivalence
I=Q.dot(Q.T)
print(I)



