import numpy as np

l = 6
p = 3
a = np.array((0, 0.1, -0.2, 0.3))
b = np.zeros(l)
b[0] = 1

for k in range(1, l):
    b[k] = sum([a[i] * b[k-i] for i in range(4) if k-i > 0])

print(b)