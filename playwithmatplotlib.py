#matplotlib
# import numpy as np
# import matplotlib.pyplot as plt

# if __name__ == '__main__':
# 	t = np.arange(0.,5.,0.2)
# 	lines = plt.plot(t, t, 'r--', t, t**2, 'bs', t, t**3, 'g^')
# 	plt.setp(lines,alpha = 0.5,animated = True)
# 	plt.axis([-1,6,-1,6])
# 	plt.grid()
# 	plt.ylabel('I am y')
# 	plt.show()
	
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt

fig = plt.figure()
ax = fig.gca(projection='3d')

x = np.linspace(0, 1, 100)
y = np.sin(x * 2 * np.pi) / 2 + 0.5
ax.plot(x, y, zs=0, zdir='z', label='zs=0, zdir=z')

colors = ('r', 'g', 'b', 'k')
for c in colors:
    x = np.random.sample(20)
    y = np.random.sample(20)
    ax.scatter(x, y, 0, zdir='y', c=c)

ax.legend()
ax.set_xlim3d(0, 1)
ax.set_ylim3d(0, 1)
ax.set_zlim3d(0, 1)

plt.show()