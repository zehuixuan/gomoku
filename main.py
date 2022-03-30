from board import Board
from move import Move
from basic import *

# Random Game
board = Board()
moves = board.legalMoves()
board.playout()
print(board.board)
print(board.existFive())
print(board.score())

#

