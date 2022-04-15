import random

Dx = 15
Dy = 15
Empty = 0
White = 1
Black = 2
numPiece = 5

MaxLegalMoves = Dx * Dy
MaxCodeLegalMoves = 2 * Dx * Dy

def add (board, Table):
    nplayouts = [0.0 for x in range (MaxLegalMoves)]
    nwins = [0.0 for x in range (MaxLegalMoves)]
    Table[board.h] = [0, nplayouts, nwins]

def look (board, Table):
    return Table.get(board.h, None)

def playoutAMAF (board, played):
    while (True):
        moves = board.legalMoves()
        if len (moves) == 0 or board.terminal ():
            return board.score ()
        n = random.randint (0, len (moves) - 1)
        played.append (moves[n].code())
        board.play (moves [n])
    
def addAMAF (board, Table):
    nplayouts = [0.0 for x in range (MaxLegalMoves)]
    nwins = [0.0 for x in range (MaxLegalMoves)]
    nplayoutsAMAF = [0.0 for x in range (MaxCodeLegalMoves)]
    nwinsAMAF = [0.0 for x in range (MaxCodeLegalMoves)]
    Table[board.h] = [0, nplayouts, nwins, nplayoutsAMAF, nwinsAMAF]

def updateAMAF (t, played, res):
    for i in range (len (played)):
        code = played [i]
        seen = False
        for j in range (i):
            if played [j] == code:
                seen = True
        if not seen:
            t [3] [code] += 1
            t [4] [code] += res

