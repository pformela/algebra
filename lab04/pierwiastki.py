import matplotlib.pyplot as plt
import numpy as np
import math

number = complex(-1, 1)
rootIndex = 3

im = [number.imag]
re = [number.real]

# x and y ranges, tick interval
xmin = -abs(re[0]) - 1
xmax = abs(re[0]) + 1
ymin = -abs(im[0]) - 1
ymax = abs(im[0]) + 1
ticks_frequency = 1

# creating axes object, figure and defining colour
fig, ax = plt.subplots(figsize=(xmax * 5, ymax * 5))
fig.patch.set_facecolor('#ffffff')

# applying ranges to axes
ax.set(xlim=(xmin-1, xmax+1), ylim=(ymin-1, ymax+1), aspect="equal")

# setting both axes to zero position
ax.spines['bottom'].set_position('zero')
ax.spines['left'].set_position('zero')

# hiding top and right spines
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

# setting labels 
ax.set_xlabel("Re", size=14, labelpad=-24, x=1.02)
ax.set_ylabel("Im", size=14, labelpad=-21, y=1.02, rotation=0)
plt.text(0.49, 0.49, r"$0$", ha='right', va='top', transform=ax.transAxes, horizontalalignment='center', fontsize=14)

# creating x and y ticks
x_ticks = np.arange(xmin, xmax+1, ticks_frequency)
y_ticks = np.arange(ymin, ymax+1, ticks_frequency)
ax.set_xticks(x_ticks[x_ticks != 0])
ax.set_yticks(y_ticks[y_ticks != 0])
ax.set_xticks(np.arange(xmin, xmax+1), minor=True)
ax.set_yticks(np.arange(ymin, ymax+1), minor=True)

# adding a grid
ax.grid(which='both', color='grey', linewidth=1, linestyle='-', alpha=0.2)

plt.grid()

x = np.empty([rootIndex])
y = np.empty([rootIndex])

module = math.sqrt(math.pow(number.real, 2) + math.pow(number.imag, 2))
angle = np.angle(number)

for k in range(0, rootIndex):
    x_pos = module ** (1. / rootIndex) * math.cos((angle + 2 * k * math.pi)/rootIndex)
    y_pos = module ** (1. / rootIndex) * math.sin((angle + 2 * k * math.pi)/rootIndex) * (1 if number.imag >= 0 else -1)

    x[k] = x_pos
    y[k] = y_pos

    # plt.plot(x_pos, y_pos, marker="o", markersize=8, markerfacecolor="green")


order = np.argsort(np.arctan2(y - y.mean(), x - x.mean()))
plt.fill(x[order], y[order], "g", alpha=0.5)

# plt.plot(re, im, marker="o", markersize=8, markerfacecolor="blue")

plt.show()