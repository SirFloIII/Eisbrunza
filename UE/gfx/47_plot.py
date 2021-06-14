import numpy as np
from matplotlib import pyplot as plt

a = 0.5
sigma = 1
T = np.arange(10)

gamma = sigma * a**T /(1-a**2)
mod4 = (T % 4) == 0

plt.plot(T, gamma*mod4, marker = "o", ls = "None")

plt.savefig("47_fig.png")
plt.show()
