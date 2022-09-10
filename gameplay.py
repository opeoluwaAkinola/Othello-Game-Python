from board import othello_board

class Gameplay:
    def __init__(self):
        self.numOfTiles = 4
        self.player1=othello_board.player1
        self.player2=othello_board.player2
        self.board=othello_board
    # Function to start the game initialising each players color, initialising the board
    # and updating the score and number of tiles on the board
    def initiliaseGameplay(self):
        # Player 1 is always black
        # Player 2 is always white
        self.player1.color_update(color='B')
        self.player2.color_update(color='W')
        self.board.updateScore()
        # End of initialise game play function

    # Function to check if a player has any valid moves at each turn of their play
    # This will help determine the end of the game if neither player has any valid
    # moves to play
    def movesAvilable(self,players):
        for i in range(self.board.size):
            for j in range(self.board.size):
                if self.board.board[i][j] == ' ':
                    for k in range(-1,2):
                        for l in range(-1,2):
                            check = self.board.validMove(players.color, k, l, i, j)
                            if check:
                                return True

        return False
        # end of check moves function

        # Function to run each player play
    def playPlayers(self,players):
        # Request user input
        print(f"{players.name}'s turn ({players.color})\n")
        check=False
        slot=input("Your move or press p to pass your turn:")
        # Check if user skips turn
        if slot.lower() != 'p':
            # check if the string entered is of a valid format and/or the move is valid and/or
            # the slot on the board is empty
            while not check:
                if not self.board.isNotEmpty(slot) or self.board.checkMove(players.color(slot)) or players.checkInput(slot):
                    check = True
                    notPass=False
                elif slot.lower() == 'p':
                    notPass=True
                    check = True
                else:
                    slot=input("Invalid move, please enter a valid slot:")
                if not notPass:
                # Implement the move
                    self.board.playerMove(players.color, slot);
                # increment the number of tiles counter, update the score and print the board
                    self.numOfTiles++1
                    self.board.updateScore()
                    self.board.printBoard()

# End of play player function
