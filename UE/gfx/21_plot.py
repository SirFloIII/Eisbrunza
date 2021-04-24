import numpy as np
from matplotlib import pyplot as plt

n = 1000

T, dt = np.linspace(0, 1, num = n, retstep=True, endpoint=False)

W = np.cumsum(np.random.normal(scale = np.sqrt(dt), size = T.shape))
W -= W[0]

steps = 5
stepsamples = n//steps
Z = np.zeros(T.shape)
for k in range(steps):
	Z[k*stepsamples:(k+1)*stepsamples] = W[k*stepsamples]
	
steps = 50
stepsamples = n//steps
Y = np.zeros(T.shape)
for k in range(steps):
	Y[k*stepsamples:(k+1)*stepsamples] = W[k*stepsamples]
	
plt.plot(T, W, T, Z, T, Y)
plt.legend(("W", "f_5", "f_50"))
plt.show()
