from basic import *
from math import sqrt
from math import log

def UCT (board):
    if board.terminal ():
        return board.score ()
    t = look (board)
    if t != None:
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
        board.play (moves [best])
        res = UCT (board)
        t [0] += 1
        t [1] [best] += 1
        t [2] [best] += res
        return res
    else:
        add (board)
        return board.playout ()