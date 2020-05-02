import numpy as np

myArray = np.array([[0, 1, 2, 3], [4, 5, 6, 7],
                    [8, 9, 10, 11], [12, 13, 14, 15]], dtype='float')

print(myArray)
print('Second row: ', myArray[1, :])
print('Third column: ', myArray[:, 2])

myArray[0:2,0:2] = 0.21
print(myArray)