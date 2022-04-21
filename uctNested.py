from basic import *
import copy
from math import sqrt
from math import log
import numpy as np

Table = {}
totalMove = 0
totalGame = 0

def UCTNested (board, t1):
    global totalMove
    global totalGame
    if board.terminal ():
        # print('calculate misere score')
        return board.misereScore () / (t1 + 1)
    t = look (board,Table)
    # print('look into Table')
    if t != None:
        # print('find a t')
        bestValue = -1000000.0
        best = 0
        moves = board.legalMoves ()
        for i in range (0, len (moves)):
            # print('this is '+str(i)+' th move')
            val = 1000000.0
            if t [1] [i] > 0:
                Q = t [2] [i] / t [1] [i]
                if board.turn == Black:
                    Q = -Q
                val = Q + 0.4 * sqrt (log (t [0]) / t [1] [i])
            if val > bestValue:
                bestValue = val
                best = i
        # print('play best move = '+str(best))
        board.play (moves [best])
        totalMove += 1
        # print('totalMove: '+str(totalMove))
        # print('enter UCTnested')
        res = UCTNested (board, t1 + 1)
        t [0] += 1
        t [1] [best] += 1
        t [2] [best] += res
        return res
    else:
        # print('add to Table')
        add (board, Table)
        totalGame += 1
        # print('totalGame: '+str(totalGame))
        return board.nestedDiscountedPlayout (t1)

def BestMoveUCTNested(board, n):
    global Table
    Table.clear()
    for i in range (n):
        # print('i: '+ str(i))
        b1 = copy.deepcopy(board)
        t1 = Dx * Dy - np.sum(b1.board == 0)
        res = UCTNested(b1, t1)
    t = look (board, Table)
    moves = board.legalMoves ()
    best = moves [0]
    bestValue = t [1] [0]
    for i in range (1, len(moves)):
        if (t [1] [i] > bestValue):
            bestValue = t [1] [i]
            best = moves [i]
    return best
