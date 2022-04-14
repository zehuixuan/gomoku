from basic import *
from math import sqrt
from math import log
import copy

Table = {}

def add (board):
    nplayouts = [0.0 for x in range (MaxLegalMoves)]
    nwins = [0.0 for x in range (MaxLegalMoves)]
    Table[board.h] = [0, nplayouts, nwins]

def look (board):
    return Table.get(board.h, None)

def UCT (board):
    if board.terminal():
        return board.score ()
    # SimTree
    t = look (board)
    if t != None:
        # SelectMove
        bestValue = -1000000.0
        best = 0
        moves = board.legalMoves ()
        for i in range (0, len (moves)):
            val = 1000000.0
            if t [1] [i] > 0:
                Q = t [2] [i] / t [1] [i]
                if board.turn == Black:
                    Q = 1 - Q
                val = Q + 0.4 * sqrt (log (t [0]) / t [1] [i])
            if val > bestValue:
                bestValue = val
                best = i
        # End of SelectMove
        board.play (moves [best])
        res = UCT (board)
        t [0] += 1
        t [1] [best] += 1
        t [2] [best] += res
        return res
    else:
        add (board)
        return board.playout ()
    # End of SimTree

def BestMoveUCT (board, n):
    global Table
    Table.clear()
    for i in range (n):
        b1 = copy.deepcopy(board)
        res = UCT(b1)
    t = look (board)
    moves = board.legalMoves ()
    best = moves [0]
    bestValue = t [1] [0]
    for i in range (1, len(moves)):
        if (t [1] [i] > bestValue):
            bestValue = t [1] [i]
            best = moves [i]
    return best