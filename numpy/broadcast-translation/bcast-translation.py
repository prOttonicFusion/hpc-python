import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt('points_circle.dat')

# Move data points by adding a vector to them
vector = np.array((3.14, 1.07))
dataTranslated = data + vector

plt.plot(data[:,0], data[:,1], 'o', label='original')
plt.plot(dataTranslated[:,0], dataTranslated[:,1], 'o', label='translated')
plt.show()