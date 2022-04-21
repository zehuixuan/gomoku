# %%
from board import Board
from move import Move
import datetime
from basic import *
from flatMC import flat
from ucb import UCB
from uct import BestMoveUCT
from rave import BestMoveRAVE
import numpy as np
# from grave import BestMoveGRAVE
from uctNested import BestMoveUCTNested

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
print(board.existFive())
board.play(Move(White,7,8))
print(board.existFive())
board.play(Move(Black,8,8))
print(board.existFive())
board.play(Move(White,6,6))
print(board.existFive())
board.play(Move(Black,6,7))
print(board.existFive())
board.play(Move(White,8,7))
print(board.existFive())
board.play(Move(Black,8,6))
print(board.existFive())
board.play(Move(White,9,6))
print(board.existFive())
board.play(Move(Black,10,5))
print(board.existFive())
board.play(Move(White,9,5))
print(board.existFive())
board.play(Move(Black,9,4))
print(board.existFive())
board.play(Move(White,8,3))
print(board.existFive())
board.play(Move(Black,8,5))
print(board.existFive())
board.play(Move(White,7,6))
print(board.existFive())
board.play(Move(Black,10,6))
print(board.existFive())
board.play(Move(White,9,8))
print(board.existFive())
board.play(Move(Black,9,7))
print(board.existFive())
board.play(Move(White,6,5))
print(board.existFive())
board.play(Move(Black,5,4))
print(board.existFive())
board.play(Move(White,10,9))
print(board.existFive())

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

# %% Grave fail
# starttime = datetime.datetime.now()
# board = Board()
# move = BestMoveGRAVE(board,10)
# board.play(move)
# endtime = datetime.datetime.now()
# print((endtime-starttime).seconds)

# %%
all = 0
for i in range(100):
    board = Board()
    board.playout()
    all += 225-np.sum(board.board == 0)
print(all/100)
# %%
starttime = datetime.datetime.now()
board = Board()
move = BestMoveUCTNested(board,100)
board.play(move)
endtime = datetime.datetime.now()
print((endtime-starttime).seconds)

# for n = 100, 
# %%
