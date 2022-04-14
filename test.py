# %%
from board import *
from move import Move
import datetime
from basic import *
from flatMC import flat
from ucb import UCB
from uct import BestMoveUCT
from rave import BestMoveRAVE

# %% test time of 1000 random games
starttime = datetime.datetime.now()
for t in range(1000):
    board = Board()
    board.playout()
endtime = datetime.datetime.now()
print((endtime-starttime).seconds)
# 97 seconds

# %% test time of one step of UCB
starttime = datetime.datetime.now()
board = Board()
move = UCB(board,10000)
board.play(move)
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

# %% test time of one step with UCT
starttime = datetime.datetime.now()
board = Board()
move = BestMoveUCT(board,1000)
board.play(move)
endtime = datetime.datetime.now()
print((endtime-starttime).seconds)
# n = 1000, 126 seconds

# %% test time of one step with Rave
starttime = datetime.datetime.now()
board = Board()
move = BestMoveRAVE(board,1000)
board.play(move)
endtime = datetime.datetime.now()
print((endtime-starttime).seconds)

# %%
