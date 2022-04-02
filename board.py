from move import Move
from basic import *
import random
import numpy as np
import copy

class Board(object):
    def __init__(self):
        self.h = 0
        self.turn = Black
        self.board = np.zeros ((Dx, Dy))

    def legalMoves(self):
        moves = []
        for i in range (0, Dx):
            for j in range (0, Dy):
                m = Move (self.turn, i, j)
                if m.valid(self):
                    moves.append (m)
        return moves

    def score (self):
        l = self.legalMoves ()
        if self.existFive()[0]:
            return self.existFive()[1]
        elif len (l) == 0:
            return 0.5
        return -1

    def terminal (self):
        if self.existFive()[0]:
            return True
        l = self.legalMoves ()
        if len (l) == 0:
            return True
        return False

    def existFive(self):
        for i in range(0, Dx):
            for j in range(0, Dy-4):
                if self.board[i][j] != 0:
                    if (self.board[i, j:(j+5)] == White*np.ones((1,5))).all():
                        return (True, 1.0)
                    if (self.board[i, j:(j+5)] == Black*np.ones((1,5))).all():
                        return (True, 0.0)
        for i in range(0, Dx-4):
            for j in range(0, Dy):
                if self.board[i][j] != 0:
                    if (self.board[i:(i+5), j] == White*np.ones((5,1))).all():
                        return (True, 1.0)
                    if (self.board[i:(i+5), j] == Black*np.ones((5,1))).all():
                        return (True, 0.0)
        for i in range(0, Dx-4):
            for j in range(0, Dy-4):
                if self.board[i][j] != 0:
                    if (self.board[i:(i+5), j:(j+5)].diagonal() == White*np.ones((1,5))).all():
                        return (True, 1.0)
                    if (self.board[i:(i+5), j:(j+5)].diagonal() == Black*np.ones((1,5))).all():
                        return (True, 0.0)
                    if (np.fliplr(self.board[i:(i+5), j:(j+5)]).diagonal() == White*np.ones((1,5))).all():
                        return (True, 1.0)
                    if (np.fliplr(self.board[i:(i+5), j:(j+5)]).diagonal() == Black*np.ones((1,5))).all():
                        return (True, 0.0)
        return (False, -1.0)

    def play (self, move):
        self.h = self.h ^ hashTable [move.color] [move.x] [move.y]
        self.h = self.h ^ hashTurn
        self.board [move.x] [move.y] = move.color
        if (move.color == White):
            self.turn = Black
        else:
            self.turn = White

    def playout(self):
        while (True):
            moves = self.legalMoves ()
            if self.terminal ():
                return self.score ()
            n = random.randint (0, len (moves) - 1)
            self.play (moves [n])

    # def misereScore (self):
    #     s = self.score ()
    #     if s == 1:
    #         return -1
    #     if s == 0:
    #         return 1
    #     return s
    #
    # def discountedPlayout (self, t):
    #     while (True):
    #         moves = self.legalMoves ()
    #         if self.terminal ():
    #             return self.misereScore () / (t + 1)
    #         n = random.randint (0, len (moves) - 1)
    #         self.play (moves [n])
    #         t = t + 1
    #
    # def nestedDiscountedPlayout (self, t):
    #     while (True):
    #         if self.terminal ():
    #             return self.misereScore () / (t + 1)
    #         moves = self.legalMoves ()
    #         bestMove = moves [0]
    #         best = -2
    #         for i in range (len (moves)):
    #             b = copy.deepcopy (self)
    #             b.play (moves [i])
    #             s = b.discountedPlayout (t)
    #             if self.turn == Black:
    #                 s = -s
    #             if s > best:
    #                 best = s
    #                 bestMove = moves [i]
    #         self.play (bestMove)
    #         t = t + 1
