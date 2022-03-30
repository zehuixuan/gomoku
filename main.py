from board import Board
from move import Move

board = Board()
moves = board.legalMoves()
board.playout()
print(board.board)
print(board.existFive())
print(board.score())