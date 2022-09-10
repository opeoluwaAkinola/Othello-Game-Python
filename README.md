# Othello-Game-Python
I decided to remake the othello game in python....i am way better at python than any other language
IMPLEMENTATION OF THE PLAYERS:
    I decided to use a a class called Player to represent each player. The class holds the player name, the player
    score and the player colour. Since it's a 2 player game, I just need two classes. These are declared
    in the player.py file also.

IMPLEMENTATION OF THE TILES:
    The tiles are just single characters. Either 'B', 'w' or ' '.

IMPLEMENTATION OF THE BOARD:

    Implementing the board was pretty straightforward.It was also a class Board and i made an object Othello-Board.
    I decide to use just one 8-row, 8-column 2d Array of characters for the entire board. This array is declared in the board.py file
    and is accessed onyly by functions in the module file. The board is initialised first to contain nothing.
    But at the start of the game, the middle tiles are initialised as follows:

                           |   |   |
                        --- --- --- ---
                           | W | B |
                        --- --- --- ---
                           | B | W |
                        --- --- --- ---
                           |   |   |
IMPLEMENTATION OF GAMEPLAY:
    I implemented the gameplay of each player in the function called playPlayer (declared in gamePlay.py).
    The function:
    --> gets the players move,
    --> checks the validity of the move,
    --> implements the number of tiles,
    --> updates the score and
    --> prints the board.


At the end of each round of the game, the scores of the players and the time and date the game was played
is added to a file on disc.
