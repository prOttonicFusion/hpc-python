import numpy as np

board = np.zeros((8,8), dtype='int')
board[0::2, 0::2] = 1
board[1::2, 1::2] = 1
print(board,'\n')

halves = np.split(board, 2, axis=0)
print(halves[0],'\n')
print(halves[1],'\n')

newBoard = np.concatenate((halves[0],halves[1]), axis=0)
print(newBoard)