import matplotlib.pyplot as plt

number = complex(5, 3)

im = number.imag
re = number.real

xmin = -abs(re) - 3
xmax = abs(re) + 3
ymin = -abs(im) - 3
ymax = abs(im) + 3

fig, ax = plt.subplots(figsize=(xmax * 2, ymax * 2))

ax.plot([re, im], 'r', ls="--", lw=1.5, alpha=0.5)

ax.set(xlim=(xmin-1, xmax+1), ylim=(ymin-1, ymax+1), aspect="equal")

ax.spines['bottom'].set_position('zero')
ax.spines['left'].set_position('zero')
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

ax.set_xlabel("Re", size=14, labelpad=-24, x=1.03)
ax.set_ylabel("Im", size=14, labelpad=-21, x=1.02, rotation=0)

# ax.set_xticks(re)
# ax.set_yticks(im)

ax.grid(which='both', color='grey', linewidth=1, linestyle='-', alpha=0.2)

plt.show()