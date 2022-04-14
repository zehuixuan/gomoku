from move import Move
from basic import *
import random
import numpy as np

hashTable = []
random.seed(42)
for k in range (3):
    l = []
    for i in range (Dx):
        l1 = []
        for j in range (Dy):
            l1.append (random.randint (0, 2 ** 64))
        l.append (l1)
    hashTable.append (l)
hashTurn = random.randint (0, 2 ** 64)

class Board(object):
    def __init__(self):
        self.h = 0
        self.turn = Black
        self.board = np.zeros ((Dx, Dy))
        self.lastMove = None

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
    
    # existFive version 4
    def existFive(self):
        if self.lastMove != None:
            check_area = np.zeros((9,9))
            x = self.lastMove.x
            y = self.lastMove.y
            color = self.lastMove.color

            if color == White:
                win_num = 1.0
            if color == Black:
                win_num = 0.0

            x_min = max([x-4,0])
            y_min = max([y-4,0])
            x_max = min([x+4,Dx-1])
            y_max = min([y+4,Dy-1])

            x_begin = max([4-x,0])
            y_begin = max([4-y,0])
            x_end = min([Dx-x+3,8])
            y_end = min([Dy-y+3,8])
            
            check_area[x_begin:x_end+1,y_begin:y_end+1] = self.board[x_min:x_max+1,y_min:y_max+1].copy()
            check_row = check_area[4,:]
            check_col = check_area[:,4]
            check_diag1 = check_area.diagonal()
            check_diag2 = check_area[::-1,:].diagonal()

            for i in range(0,5):
                if (check_row[i:(i+5)] == color*np.ones(5)).all():
                    return (True, win_num)
                if (check_col[i:(i+5)] == color*np.ones(5)).all():
                    return (True, win_num)
                if (check_diag1[i:(i+5)] == color*np.ones(5)).all():
                    return (True, win_num)
                if (check_diag2[i:(i+5)] == color*np.ones(5)).all():
                    return (True, win_num)
        return (False, -1.0)

    # existFive version 3
    # def existFive(self):
    #     if self.turn == Black:
    #         check_color = White
    #         win_num = 1.0
    #     if self.turn == White:
    #         check_color = Black
    #         win_num = 0.0
    
    #     check_row = (self.board==check_color).sum(axis = 1)>=5
    #     check_col = (self.board==check_color).sum(axis = 0)>=5
    #     check_diag = np.array([(self.board.diagonal(i)==check_color).sum()>=5 for i in range(-Dx+5,Dx-4)])
    #     check_diaginv = np.array([(self.board[::-1,:].diagonal(i)==check_color).sum()>=5 for i in range(-Dx+5,Dx-4)])
    #     for i in range(0, Dx):
    #         if check_row[i]:
    #             for j in range(0, Dy-4):
    #                 if self.board[i][j] == check_color:
    #                     if (self.board[i, j:(j+5)] == check_color*np.ones((1,5))).all():
    #                         return (True, win_num)
    #     for j in range(0, Dy):
    #         if check_col[j]:
    #             for i in range(0, Dx-4):
    #                 if self.board[i][j] == check_color:
    #                     if (self.board[i:(i+5), j] == check_color*np.ones((5,1))).all():
    #                         return (True, win_num)
    #     for k in range(-Dx+5,Dx-4):
    #         if check_diag[k]:
    #             diag = self.board.diagonal(k)
    #             for d in range(0, len(diag)):
    #                 if diag[d] == check_color:
    #                     if (diag[:,d:(d+5)] == check_color*np.ones((1,5))).all():
    #                         return (True, win_num)
    #     for k in range(-Dx+5,Dx-4):
    #         if check_diaginv[k]:
    #             diag = self.board[::-1,:].diagonal(k)
    #             for d in range(0, len(diag)):
    #                 if diag[d] == check_color:
    #                     if (diag[:,d:(d+5)] == check_color*np.ones((1,5))).all():
    #                         return (True, win_num)
    #     return (False, -1.0)

    # existFive version 2
    # def existFive(self):
    #     for i in range(0, Dx):
    #         for j in range(0, Dy-4):
    #             if self.board[i][j] != 0:
    #                 if (self.board[i, j:(j+5)] == White*np.ones((1,5))).all():
    #                     return (True, 1.0)
    #                 if (self.board[i, j:(j+5)] == Black*np.ones((1,5))).all():
    #                     return (True, 0.0)
    #     for i in range(0, Dx-4):
    #         for j in range(0, Dy):
    #             if self.board[i][j] != 0:
    #                 if (self.board[i:(i+5), j] == White*np.ones((5,1))).all():
    #                     return (True, 1.0)
    #                 if (self.board[i:(i+5), j] == Black*np.ones((5,1))).all():
    #                     return (True, 0.0)
    #     for i in range(0, Dx-4):
    #         for j in range(0, Dy-4):
    #             if self.board[i][j] != 0:
    #                 if (self.board[i:(i+5), j:(j+5)].diagonal() == White*np.ones((1,5))).all():
    #                     return (True, 1.0)
    #                 if (self.board[i:(i+5), j:(j+5)].diagonal() == Black*np.ones((1,5))).all():
    #                     return (True, 0.0)
    #                 if (np.fliplr(self.board[i:(i+5), j:(j+5)]).diagonal() == White*np.ones((1,5))).all():
    #                     return (True, 1.0)
    #                 if (np.fliplr(self.board[i:(i+5), j:(j+5)]).diagonal() == Black*np.ones((1,5))).all():
    #                     return (True, 0.0)
    #     return (False, -1.0)

    # existFive version 1
    # def existFive(self):
    #     for i in range(0, Dx):
    #         for j in range(0, Dy-4):
    #             if (self.board[i, j:(j+5)] == White*np.ones((1,5))).all():
    #                 return (True, 1.0)
    #             if (self.board[i, j:(j+5)] == Black*np.ones((1,5))).all():
    #                 return (True, 0.0)
    #     for i in range(0, Dx-4):
    #         for j in range(0, Dy):
    #             if (self.board[i:(i+5), j] == White*np.ones((5,1))).all():
    #                 return (True, 1.0)
    #             if (self.board[i:(i+5), j] == Black*np.ones((5,1))).all():
    #                 return (True, 0.0)
    #     for i in range(0, Dx-4):
    #         for j in range(0, Dy-4):
    #             if (self.board[i:(i+5), j:(j+5)].diagonal() == White*np.ones((1,5))).all():
    #                 return (True, 1.0)
    #             if (self.board[i:(i+5), j:(j+5)].diagonal() == Black*np.ones((1,5))).all():
    #                 return (True, 0.0)
    #             if (np.fliplr(self.board[i:(i+5), j:(j+5)]).diagonal() == White*np.ones((1,5))).all():
    #                 return (True, 1.0)
    #             if (np.fliplr(self.board[i:(i+5), j:(j+5)]).diagonal() == Black*np.ones((1,5))).all():
    #                 return (True, 0.0)
    #     return (False, -1.0)


    def play (self, move):
        self.h = self.h ^ hashTable [move.color] [move.x] [move.y]
        self.h = self.h ^ hashTurn
        self.board [move.x] [move.y] = move.color
        self.lastMove = move
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
