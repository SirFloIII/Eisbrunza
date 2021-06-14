import numpy as np
from scipy import linalg as lin

gamma = np.array((8.952,
                  7.870,
                  7.083,
                  6.562,
                  6.036,
                  5.537,
                  5.086,
                  4.673,
                  4.292,
                  3.942))

def prognose(h, k):
    GAMMA = lin.toeplitz(gamma[0:k])
    c = gamma[h:h+k] @ lin.inv(GAMMA)
    err = gamma[0] - c @ GAMMA @ c.T
    return c, err

for p in range(1, 10):
    a, err = prognose(1, p)
    print(f"{p=}: {err=}")
    print(f"{a=}\n")