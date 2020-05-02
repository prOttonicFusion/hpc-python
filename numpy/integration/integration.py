import numpy as np

# Approximate integrals using the middle Riemann sum

dx = 0.1
x0 = 0.0
xn = np.pi/2
xi = np.arange(x0, xn, dx)
xip = (xi[1:] + xi[:-1])/2

riemannSum = sum(np.sin(xip)*dx)

print('For dx = {} the Riemann sum of sin(x) in ({:.6}, {:.6}) has a value of {:.6}'.format(dx, x0, xn, riemannSum))