# %%
from board import Board
from move import Move
import datetime
from basic import *
from flatMC import *
from ucb import *
from uct import *

# %%
# test time of one step of UCB
starttime = datetime.datetime.now()
board = Board()
m_flat = UCB(board,10000)
board.play(m_flat)
endtime = datetime.datetime.now()
print((endtime-starttime).seconds)
# n = 1000, 106 seconds
# n = 10000, 1034 seconds

# %%
# test if it can detect the Five
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

# %% test time of 1000 random games
starttime = datetime.datetime.now()
for t in range(1000):
    board = Board()
    board.playout()
endtime = datetime.datetime.now()
print((endtime-starttime).seconds)
# 97 seconds
