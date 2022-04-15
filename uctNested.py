from basic import *
import copy
from math import sqrt
from math import log
import numpy as np

Table = {}

def UCTNested (board, t1):
    if board.terminal ():
        return board.misereScore () / (t1 + 1)
    t = look (board,Table)
    if t != None:
        bestValue = -1000000.0
        best = 0
        moves = board.legalMoves ()
        for i in range (0, len (moves)):
            val = 1000000.0
            if t [1] [i] > 0:
                Q = t [2] [i] / t [1] [i]
                if board.turn == Black:
                    Q = -Q
                val = Q + 0.4 * sqrt (log (t [0]) / t [1] [i])
            if val > bestValue:
                bestValue = val
                best = i
        board.play (moves [best])
        res = UCTNested (board, t1 + 1)
        t [0] += 1
        t [1] [best] += 1
        t [2] [best] += res
        return res
    else:
        add (board, Table)
        return board.nestedDiscountedPlayout (t1)

def BestMoveUCTNested(board, n):
    global Table
    Table.clear()
    for i in range (n):
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
