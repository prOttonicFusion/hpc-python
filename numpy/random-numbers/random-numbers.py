import numpy as np
import matplotlib.pyplot as plt

print('Uniform random distribution:')
randVals = np.random.rand(1000)
plt.hist(randVals)
plt.show()
print('  Mean: ', np.mean(randVals))
print('  Std:  ', np.std(randVals))

print('Normal random distribution:')
randVals = np.random.normal(1000)
plt.hist(randVals)
plt.show()
print('  Mean: ', np.mean(randVals))
print('  Std:  ', np.std(randVals))