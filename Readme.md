# Class Board

## Attribute
- h: Hashcode. Used in transposition table.
- turn: White or Black. Indicate which player should play.
- board: 2d-array, 15 * 15. Initialize with zeros.
- lastMove: Last played move. Initialize with None.

## Methods
- `legalMoves()`: Return a list of legal `Move` (all the empty places)
- `score()`: Return the score of the game. 
  - Return 1 or 0, if there is a winner (the first time that there are five pieces on a line).
    - 1: Winner is White.
    - 0: Winner is Black.
  - Return -1 if the game is not over.
  - Return 0.5 if two players are tied. (all places have pieces but no 5 pieces are on a line)
- `terminal()`: Return a boolean to indicate whether the game is over.
- `existFive()`: Return a tuple of a boolean and a float. 
  - The boolean indicates if there are 5 pieces on a line.
  - The float indicate which player made the 5 pieces on a line. (-1 means that there are no 5 pieces on a line)
- `play(move)`: Play a move.
- `playout()`: Play random game for the rest of the game. Return the score of final result.
- `misereScore()`: Return the misere score of the game.
  -  -1: Winner is Black.
  -  1: Winner is White.
  -  -100: The game is not over.
-  `discountedPlayout(t)`: Play random game for the rest of the game. Return the discounted score of final result.
-  `nestedDiscountedPlayout(t)`: Use `discountedPlayout` to decide the best move until the end of game. Return the discounted score of final result.

# Class Move
## Attribute
- color: White or Black.
- x and y: Coordinates for placing the pieces
## Methods
- `valid(board)`: Return a boolean to indicate whether this move can be played on this board.
- `code()`: Return a code associate this move.
