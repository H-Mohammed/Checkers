# English Checkers
Checkers is a strategy board games consisting of two players involving the diagonal movement of pieces.
This game of checkers is based off of the English version, as such it will be using the English rules.

You can play the game against a computer or another player.

### How to play:
 - You can only move diagonally one step forwards, never backwards (with the exception of the king).
 - You can only move onto black spaces.
 - You must capture a piece if you can.
    - To capture a piece, you make two steps diagonally instead of one and the space beyond the target must be __unoccupied.__
    - Upon capturing a piece, you receive an extra move with the piece that you captured with, allowing consecutive captures.
 - Upon reaching the opposite side of the board with a piece, you are able to crown that piece to be king.
    - Kings can move both backwards and forwards diagonally.
    - Flying kings are not allowed.
 - To win a game, you must capture all of the opponent's pieces or force them into a position where a legal move is no longer possible.
    - You must still be able to make a move afterwards however, you cannot get yourself stuck.
    - The game ends in a draw if either sides can't force a win.

## Development to-do list:
 - [ ] Crowning
 - [X] Piece Movement
 - [X] Capturing
    - [ ] Ensured capturing system
 - [ ] Two player multiplayer
    - [ ] Swapping the board
 - [ ] A.I player

## Variables 
 - checkerBoard
    - Represents the checkerboard object
 - enemy
    - This is the player object that stores the enemy pieces
 - HEIGHT
    - The height of the display
 - local
    - This is the player object that stores the local pieces
 - output
    - This is a tuple of the selected piece for the enemy
    - (id, pos)
 - player_id
    - Stores the player id of client
 - turn
    - Represents the player turn
    - 1 denotes YOUR turn
    - 2 denotes ENEMY turn
 - ui
    - This is the main object for the user interface
 - WIDTH
    - The width of the display
 - window
    - This is the main display where all of our assets are placed
## Classes
 - Background
    - Use this to make the background for text
 - Checker
    - Use this to make checker pieces
 - Container
    - Parent class for all objects that store other objects
 - Network
    - This class is responsible for all the networking
 - Objects 
    - The parent class used to make any items
 - Parent
    - Just a generic parent class
 - Player
    - Stores the client's friendly pieces
 - Star
    - Use this to make the star which indicates where the player can move
 - Square
    - Use this to make the squares for the board
 - Text
    - Use this to make text