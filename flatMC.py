from basic import *
import copy

def flat (board, n):
    moves = board.legalMoves()
    bestScore = 0
    bestMove = 0
    for m in range(len(moves)):
        sum = 0
        for i in range (n):
            b = copy.deepcopy (board)
            b.play (moves [m])
            r = b.playout ()
            if board.turn == Black:
                r = 1 - r
            sum = sum + r
        if sum > bestScore:
            bestScore = sum
            bestMove = m
    return moves[bestMove]