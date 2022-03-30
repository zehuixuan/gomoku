import random

Dx = 15
Dy = 15
Empty = 0
White = 1
Black = 2

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