import numpy as np
from matplotlib import pyplot as plt

n = 400

T, dt = np.linspace(0, 4, num = n, retstep=True, endpoint=False)

W = np.cumsum(np.random.normal(scale = np.sqrt(dt), size = T.shape))
W -= W[0]

Z = np.zeros(T.shape)
Z[    n//4 : 2 * n//4] = W[    n//4]
Z[2 * n//4 : 3 * n//4] = W[2 * n//4]


plt.plot(T, W, T, Z)
plt.legend(("W", "Z"))
plt.show()
