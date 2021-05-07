import numpy as np
from matplotlib import pyplot as plt


T = np.arange(10)

for _ in range(3):
    A, B = np.random.normal(size = 2)
    X = A + (-1)**T * B

    plt.plot(T, X, marker = "o", ls = "--", label = f"{A = :.2f}, {B = :.2f}")
    plt.legend()
    

plt.savefig("33_fig.png")
plt.show()
