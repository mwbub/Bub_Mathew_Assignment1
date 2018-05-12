
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.axes3d import Axes3D
from matplotlib import cm

def f(x, y, npoints):
    c = x + y*1j
    z = 0
    yield np.zeros(c.shape)
    for i in range(npoints):
        z = z**2 + c
        yield z

lower, upper = -2, 2
x = np.linspace(lower, upper, 1000)
xv, yv = np.meshgrid(x, x)
npoints = 10
vals = list(f(xv, yv, npoints))

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1, projection='3d')
ax.set_xlabel('$x$')
ax.set_ylabel('$y$')
ax.set_zlabel('$\log_{10}(|z_{%d}|)$'%(npoints))
ax.set_title('Absolute Value of $z_{%d}$'%(npoints))
surf = ax.plot_surface(xv, yv, np.log10(abs(vals[npoints])), cmap = cm.jet)
