from matplotlib.lines import Line2D
import matplotlib.pyplot as plt
import numpy as np
import math

number = complex(5,3)

im = [number.imag]
re = [number.real]

# x and y ranges, tick interval
xmin = -abs(re[0]) - 3
xmax = abs(re[0]) + 3
ymin = -abs(im[0]) - 3
ymax = abs(im[0]) + 3
ticks_frequency = 1

# creating axes object, figure and defining colour
fig, ax = plt.subplots(figsize=(xmax * 2, ymax * 2))
fig.patch.set_facecolor('#ffffff')

# ax.plot([re, im], 'r', ls="--", lw=1.5, alWpha=0.5)

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

# line_1 = Line2D([0, 0], [re[0], im[0]], linewidth=1, linestyle="-", color="green")
# line_2 = Line2D([re[0], 0], [0, 0], linewidth=5, linestyle="-", color="black")

# ax.add_line(line_1)
# ax.add_line(line_2)

angle = np.angle(number)
print(angle * 100)

a1, b1 = (3/5), 0
a2, b2 = (0), 0

plt.grid()
plt.plot(ax, ax*a1 + 0)
plt.plot(ax, ax*a2 + 0)

plt.show()