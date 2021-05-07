import numpy as np
from matplotlib import pyplot as plt
from collections import defaultdict


T = np.arange(-4, 5)

a = defaultdict(float)
a[0] = 1
a[-1] = 0.8
a[1]  = 0.8

b = defaultdict(lambda:1)

c = defaultdict(float)
c[0] = 1
c[1] = 0.25
c[-1] = -0.25

d = dict()
for t in T:
    d[t] = 1.25**abs(t)


for e in ["a", "b", "c", "d"]:
    plt.plot(T, [globals()[e][t] for t in T], marker = "o", ls = "--", label = f"${e}_k$")


plt.legend()

plt.savefig("34_fig.png")
plt.show()
