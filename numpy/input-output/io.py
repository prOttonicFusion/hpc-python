import numpy as np

xy = np.loadtxt('xy-coordinates.dat')

xy[:,1] += 2.5 # Add 2.5 to y values

np.savetxt('xy-coordinates_edited.dat', xy, header='x y', fmt='%.7f')