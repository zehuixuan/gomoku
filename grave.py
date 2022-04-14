from basic import *
import copy

Table = {}

def GRAVE (board, played, tref):
    if (board.terminal ()):
        return board.score ()
    t = look (board, Table)
    if t != None:
        tr = tref
        if t [0] > 50:
            tr = t
        bestValue = -1000000.0
        best = 0
        moves = board.legalMoves ()
        bestcode = moves [0].code ()
        for i in range (0, len (moves)):
            val = 1000000.0
            code = moves [i].code ()
            if tr [3] [code] > 0:
                beta = tr [3] [code] / (t [1] [i] + tr [3] [code] + 1e-5 * t [1] [i] * tr [3] [code])
                Q = 1
                if t [1] [i] > 0:
                    Q = t [2] [i] / t [1] [i]
                    if board.turn == Black:
                        Q = 1 - Q
                AMAF = tr [4] [code] / tr [3] [code]
                if board.turn == Black:
                    AMAF = 1 - AMAF
                val = (1.0 - beta) * Q + beta * AMAF
            if val > bestValue:
                bestValue = val
                best = i
                bestcode = code
        board.play (moves [best])
        played.append (bestcode)
        res = GRAVE (board, played, tr)
        t [0] += 1
        t [1] [best] += 1
        t [2] [best] += res
        updateAMAF (t, played, res)
        return res
    else:
        addAMAF (board, Table)
        return playoutAMAF (board, played)

# def BestMoveGRAVE (board, n):
#     global Table
#     Table.clear()
#     for i in range (n):
#         b1 = copy.deepcopy (board)
#         res = GRAVE (b1, [], None)
#     t = look (board, Table)
#     moves = board.legalMoves ()
#     best = moves [0]
#     bestValue = t [1] [0]
#     for i in range (1, len(moves)):
#         if (t [1] [i] > bestValue):
#             bestValue = t [1] [i]
#             best = moves [i]
#     return best