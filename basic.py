import random

Dx = 15
Dy = 15
Empty = 0
White = 1
Black = 2

MaxLegalMoves = Dx * Dy
Table = {}

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

def add (board):
    nplayouts = [0.0 for x in range (MaxLegalMoves)]
    nwins = [0.0 for x in range (MaxLegalMoves)]
    Table[board.h] = [0, nplayouts, nwins]

def look (board):
    return Table.get(board.h, None)