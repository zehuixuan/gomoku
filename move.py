from constant import *

class Move(object):
    def __init__(self, color, x, y):
        self.color = color
        self.x = x
        self.y = y

    def valid (self, board):
        if self.x >= Dx or self.y >= Dy or self.x < 0 or self.y < 0:
            return False
        if board.board[self.x][self.y] == Empty:
            return True
        return False

    # def code (self, board):
        # direction = 0
        # if self.y2 > self.y1:
        #     if board.board [self.x2] [self.y2] == Empty:
        #         direction = 1
        #     else:
        #         direction = 2
        # if self.y2 < self.y1:
        #     if board.board [self.x2] [self.y2] == Empty:
        #         direction = 3
        #     else:
        #         direction = 4
        # if self.color == White:
        #     return 5 * (Dy * self.x1 + self.y1) + direction
        # else:
        #     return 5 * Dx * Dy + 5 * (Dy * self.x1 + self.y1) + direction