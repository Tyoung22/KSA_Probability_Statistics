import sys
input = lambda: sys.stdin.readline().rstrip()
from random import shuffle

import numpy as np
import matplotlib.pyplot as plt

res = []

for N in range(1, 101):
    print(N)
    ex = []
    for _ in range(100000):
        man = [i for i in range(N)]
        women = [i for i in range(N)]
        shuffle(man); shuffle(women)
        count = 0

        for i in range(N):
            if man[i] == women[i] or man[i] == women[i-1]: count += 1
        ex.append(count)
    res.append(np.mean(ex))

print(res)
plt.plot(res)