# English Checkers
Checkers is a strategy board games consisting of two players involving the diagonal movement of pieces.
This game of checkers is based off of the English version, as such it will be using the English rules.

You can play the game against a computer or another player.

### How to play:
 - You can only move diagonally one step forwards, never backwards (with the exception of the king).
 - You can only move onto black spaces.
 - You must capture a piece if you can.
    - To capture a piece, you make two steps diagonally instead of one and the space beyond the target must be _unoccupied._
    - Upon capturing a piece, you receive an extra move with the piece that you captured with, allowing consecutive captures.
 - Upon reaching the opposite side of the board with a piece, you are able to crown that piece to be king.
    - Kings can move both backwards and forwards diagonally.
    - Flying kings are not allowed.
 - To win a game, you must capture all of the opponent's pieces or force them into a position where a legal move is no longer possible.
    - You must still be able to make a move afterwards however, you cannot get yourself stuck.
    - The game ends in a draw if either sides can't force a win.

## Variables 
 - HEIGHT
    - The height of the display
 - WIDTH
    - The width of the display
 - window
    - This is the main display where all of our assets are placed
## Classes
 - Checker
    - Use this to make checker pieces
 - Container
    - Parent class for all objects that store other objects
 - Network
    - This class is responsible for all the networking
 - Objects 
    - The parent class used to make any items
 - Player
    - Stores pieces
 - Square
    - Use this to make the squares for the board