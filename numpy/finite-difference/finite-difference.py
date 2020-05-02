import numpy as np
import matplotlib.pyplot as plt

# Evaluate numerically the derivative of sin(x) where x = (0, pi/2)
dx = 0.1
x = np.arange(0, np.pi/2, dx)
dsinx = (np.sin(x + dx) - np.sin(x - dx)) / (2 * dx)
print(dsinx)

# Repeat for cos(x)
dcosx = (np.cos(x + dx) - np.cos(x - dx)) / (2 * dx)


# Plot
plt.plot(x, np.sin(x), label='sin(x)')
plt.plot(x, dsinx, label='d/dx sin(x)')
plt.plot(x, np.cos(x), '--', label='cos(x)')
plt.plot(x, dcosx, '--', label='d/dx cos(x)')
plt.xlabel("x")
plt.ylabel("y(x)")
plt.legend()
plt.show()
