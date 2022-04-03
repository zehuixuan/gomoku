from board import Board
import datetime
from basic import *
from flatMC import flat
from ucb import UCB


# test time of one step
starttime = datetime.datetime.now()
board = Board()
if board.turn == White:
    m_flat = UCB(board,100)
    board.play(m_flat)
else:
    m_ucb = UCB(board,100)
    board.play(m_ucb)
# for i in range(50):
#     board = Board()
#     board.playout()
endtime = datetime.datetime.now()
print((endtime-starttime).seconds)