import copy
import math
from basic import *

def UCB (board, n):
    moves = board.legalMoves ()
    sumScores = [0.0 for x in range (len (moves))]
    nbVisits = [0 for x in range (len(moves))]
    for i in range (n):
        bestScore = 0
        bestMove = 0
        for m in range (len(moves)):
            score = 1000000
            if nbVisits [m] > 0:
                score = sumScores [m] / nbVisits [m] + 0.4 * math.sqrt (math.log (i) / nbVisits [m])
            if score > bestScore:
                bestScore = score
                bestMove = m
        b = copy.deepcopy (board)
        b.play (moves [bestMove])
        r = b.playout ()
        if board.turn == Black:
            r = 1.0 - r
        sumScores [bestMove] += r
        nbVisits [bestMove] += 1
    bestScore = 0
    bestMove = 0
    for m in range (len(moves)):
        score = nbVisits [m]
        if score > bestScore:
            bestScore = score
            bestMove = m
    return moves [bestMove]