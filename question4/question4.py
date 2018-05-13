
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.axes3d import Axes3D

def Z(x, y, npoints):
    """ Iterate z_(i+1) = (z_i)^2 + c, where z_0 = 0 and c = x + iy. """
    c = x + y*1j
    z = 0
    for i in range(npoints):
        z = z**2 + c
        yield z
        
def isDiverging(x, y, z):
    c = x + y*1j
    return (abs(z) > abs(c) + 1)

x = np.linspace(-3, 2, 1000)
y = np.linspace(-2, 2, 1000)
xv, yv = np.meshgrid(x, y)
vals = list(Z(xv, yv, 10))


i = 10
zv = np.log10(abs(vals[i-1]))
fig = plt.figure(figsize=(10,8))
ax = fig.add_subplot(111, projection='3d')
ax.set_xlabel('$x$', fontsize = 14)
ax.set_ylabel('$y$', fontsize = 14)
ax.set_zlabel('$\log_{10}(|z_{%d}|)$'%i, fontsize = 14)
ax.set_title('Absolute value of $z_{%d}$ evaluated at $c=x+iy$'%i, 
             fontsize = 15)
surf = ax.plot_surface(xv, yv, zv, cmap = 'jet')

mask = isDiverging(xv, yv, vals[i-1])
diverging = np.log10(abs(np.where(mask, vals[i-1], np.nan)))
converging = np.log10(abs(np.where(~mask, vals[i-1], np.nan)))

fig = plt.figure(figsize=(10,8))
ax = fig.add_subplot(111, projection='3d')
ax.set_xlabel('$x$', fontsize = 14)
ax.set_ylabel('$y$', fontsize = 14)
ax.set_zlabel('$\log_{10}(|z_{%d}|)$'%i, fontsize = 14)
ax.set_title('Absolute value of $z_{%d}$ evaluated at $c=x+iy$'%i, fontsize = 15)
minval, maxval = np.min(zv), np.max(zv)
surf1 = ax.plot_wireframe(xv, yv, diverging, color = 'red')
surf2 = ax.plot_wireframe(xv, yv, converging, color = 'blue')

masks = []
earlier = np.full(vals[0].shape, False)
for j in range(1, i):
    mask = isDiverging(xv, yv, vals[j])
    masks.append(mask & ~earlier)
    earlier = earlier | mask
masks.append(~earlier)
masks = np.array(masks)
masked_vals = np.where(masks, vals[i-1], np.nan)
zv = np.log10(abs(masked_vals))

cmap = plt.get_cmap('jet')
colours = cmap(np.linspace(1, 0, i)) # get i evenly spaced colours from a colour map
fig = plt.figure(figsize=(10,8))
ax = fig.add_subplot(111, projection='3d')
ax.set_xlabel('$x$', fontsize = 14)
ax.set_ylabel('$y$', fontsize = 14)
ax.set_zlabel('$\log_{10}(|z_{%d}|)$'%i, fontsize = 14)
ax.set_title('Absolute value of $z_{%d}$ evaluated at $c=x+iy$'%i, fontsize = 15)
surfs = [ax.plot_wireframe(xv, yv, zv[j], color = colours[j], label = 'Diverged at $z_{%d}$'%(j+1)) for j in range(i-1)]
surfs.append(ax.plot_wireframe(xv, yv, zv[-1], color = colours[-1], label = 'Bounded'))
legend = ax.legend(bbox_to_anchor = (1.05, 1), loc = 2)
plt.show()

