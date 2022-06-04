from matplotlib import pyplot as plt
import numpy as np

n = 10

x_vals = np.arange(1, n+1, 1)
y_vals = np.random.randint(1, n+1, size=10)
y_valslist = []

for j in range(n):
    for i in range(n-1):
        if y_vals[i] > y_vals[i+1]:
            y_vals[i],y_vals[i+1] = y_vals[i+1],y_vals[i]
            y_valslist.append(y_vals)

for list in y_valslist:
    plt.bar(x_vals, list)
    plt.savefig('sorts/{list}.png'.format(list=list))