import numpy as np

# (1)
myList = [1.1, 2, 3.2, 4, 5, 6.8]
myFirstArray = np.array(myList)
print(myFirstArray)

# (2)
mySecondArray = np.arange(-2.0, 2.0, step=0.2)
print(mySecondArray)

# (3)
myThirdArray = np.linspace(0.5, 1.5, num=11)
print(myThirdArray)

# (4)
greeting = 'Hello, World!'
myFourthArray = np.array(greeting, dtype='c')
print(myFourthArray)