from numpy import array
from math import inf
from numpy.linalg import norm 

a=array([1, 2, 3, 4])
print(a)

maxnorm=norm(a, inf)
print(maxnorm)