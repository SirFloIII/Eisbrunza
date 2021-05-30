import numpy as np
import scipy.linalg as lin

gamma = np.array((1.83,
                 -0.19,
                 -0.09,
                  0.91,
                 -0.10,
                  0,0,0,0,0,0))

# h ... wie weit schau ich in die zukunft
# k ... wie viele punkte aus der vergangenheit schau ich an
# gamma[h:h+k] == c @ GAMMA[0:k]
def prognose(h, k):
    GAMMA = lin.toeplitz(gamma[0:k])
    c = gamma[h:h+k] @ lin.inv(GAMMA)
    err = gamma[0] - c @ GAMMA @ c.T
    return c, err

print("\\begin{table}")
print("h", "k", "\\sigma_{h,k}^2", *[f"c_{i}" for i in range(1,6)], sep = " & ", end = " \\\\\n")
for h, k in zip((1,3,5,1,3,5), (1,1,1,5,5,5)):
    c, err = prognose(h, k)
    print(h, k, f"{err:1.3f}", *[f"{cc:1.3f}" for cc in c], sep = " & ", end = " \\\\\n")
print("\\end{table}")


