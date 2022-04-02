from board import Board
from move import Move
from basic import *
from flatMC import flat
from ucb import UCB
import datetime

# # # Random Game
# board = Board()
# board.playout()
# print(board.board)
# print(board.existFive())
# print(board.score())

# # # flat Monte Carlo play against UCB
# White : flat Monte Carlo
# Black : UCB

# board = Board()
# terminal = False
# count = 0
# while not terminal:
#     count = count +1
#     print(count)
#     if board.turn == White:
#         m_flat = flat(board,100)
#         board.play(m_flat)
#     else:
#         m_ucb = UCB(board,100)
#         board.play(m_ucb)
#     terminal = board.terminal()
#     if terminal:
#         print('the winner is: ')
#         print(board.score())

# test time of one step
board = Board()
starttime = datetime.datetime.now()
if board.turn == White:
    m_flat = flat(board,100)
    board.play(m_flat)
else:
    m_ucb = UCB(board,100)
    board.play(m_ucb)
endtime = datetime.datetime.now()
print(endtime-starttime).seconds


