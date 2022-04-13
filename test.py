# %%
from board import Board
from move import Move
import datetime
from basic import *
from flatMC import flat
from ucb import UCB

# %%
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

# %%
# test accuracy
board = Board()
board.play(Move(Black,7,7))
board.existFive()
board.play(Move(White,7,8))
board.existFive()
board.play(Move(Black,8,8))
board.existFive()
board.play(Move(White,6,6))
board.existFive()
board.play(Move(Black,6,7))
board.existFive()
board.play(Move(White,8,7))
board.existFive()
board.play(Move(Black,8,6))
board.existFive()
board.play(Move(White,9,6))
board.existFive()
board.play(Move(Black,10,5))
board.existFive()
board.play(Move(White,9,5))
board.existFive()
board.play(Move(Black,9,4))
board.existFive()
board.play(Move(White,8,3))
board.existFive()
board.play(Move(Black,8,5))
board.existFive()
board.play(Move(White,7,6))
board.existFive()
board.play(Move(Black,10,6))
board.existFive()
board.play(Move(White,9,8))
board.existFive()
board.play(Move(Black,9,7))
board.existFive()
board.play(Move(White,6,5))
board.existFive()
board.play(Move(Black,5,4))
board.existFive()
board.play(Move(White,10,9))
board.existFive()
# %%
