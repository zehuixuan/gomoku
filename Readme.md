# Class Board

## Attribute
- h: Hashcode. Used in transposition table.
- turn: White or Black. Indicate which player should play.
- board: 2d-array, 15 * 15. Initialize with zeros.

## Methods
- `legalMoves()`: Return a list of legal `Move` (all the empty places)
- `score()`: Return the score of the game. 
  - Return 1 or 0 if there is a winner (the first time on the board there exists 5 pieces in a series)
  - Return -1 if the game hasn't finished.
  - Return 0.5 if two players are tied. (All places have pieces but there isn't 5 pieces in a series)
- `terminal()`: Return a boolean to indicate whether the game is over or not.
- `existFive()`: Return a tuple of a boolean and a float. 
  - The boolean indicate whether there exists 5 pieces in a series or not.
  - The float indicate which player made the 5 pieces in a series. (-1 means no 5 pieces in a series)
- `play(move)`: Play a move.
- `playout()`: Play random game for the rest of the game.

# Class Move
## Attribute
- color: White or Black.
- x and y: Coordinates for placing the pieces
## Methods
- `valid(board)`: Return a boolean to indicate whether this move can be played on this board.