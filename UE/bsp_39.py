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
    return gamma[h:h+k] @ lin.inv(GAMMA)

print("\\begin{table}")
print("h", "k", *[f"c_{i}" for i in range(1,6)], sep = " & ", end = " \\\\\n")
for h, k in zip((1,3,5,1,3,5), (1,1,1,5,5,5)):
    c = prognose(h, k)
    print(h, k, *[f"{cc:1.3f}" for cc in c], sep = " & ", end = " \\\\\n")
print("\\end{table}")
