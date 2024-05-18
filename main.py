import matplotlib.pyplot as plt
import numpy as np

u = []
xlist = []
zlist = []

with open("u.txt") as f:
    for line in f:
        u.append([float(x) for x in line.split()])
with open("x.txt") as f:
    for line in f:
        xlist.append([float(x) for x in line.split()])
with open("z.txt") as f:
    for line in f:
        zlist.append([float(x) for x in line.split()])


plt.contourf(zlist, xlist, u)
plt.show()