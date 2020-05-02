import numpy as np

board = np.zeros((8,8), dtype='int')
board[0::2, 0::2] = 1
board[1::2, 1::2] = 1
print(board)