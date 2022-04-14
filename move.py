from basic import *

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

    def code (self):
        if self.color == White:
            return (Dy * self.x + self.y)
        else:
            return Dx * Dy + (Dy * self.x + self.y)