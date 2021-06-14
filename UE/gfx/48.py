l = 7
p = 2
a = (0, +0.2, +0.4)
b = [0]*l

b[0] = 1
for k in range(1, l):
    b[k] = sum([a[i] * b[k-i] for i in range(1, p+1) if k-i >= 0])

print("\nb = ", b)

###############################
sigmasq = 1
import numpy as np
from scipy import linalg as lin
from itertools import product

A = np.eye(l)
for i, j in product(range(l), range(l)):
    if 0 < i+j <= p:
        A[i,j] -= a[i+j]
    if j > 0 and 0 < i-j <= p:
        A[i,j] -= a[i-j] 
b = np.array([sigmasq]+[0]*(l-1))
y = np.linalg.solve(A, b)

print("\nA := ", A)
print("\ngamma = ", y)