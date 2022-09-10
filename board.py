# Created by Opeoluwa Akinola

# Define number of boards
from player import player_1, player_2
SIZE = 8


# Create Board class
class Board:
    # Initialise board, wince it is othello, it always starts with 2-white tiles and 2-black tiles
    def __init__(self):
        self.size=SIZE
        self.board = [[' ' for x in range(SIZE)] for y in range(SIZE)]
        # Since it is Othello, there are 4 pieces already in the board at the start of the game
        self.board[3][3] = 'W'
        self.board[3][4] = 'B'
        self.board[4][3] = 'B'
        self.board[4][4] = 'W'
        self.player1=player_1
        self.player2=player_2
        # End of initilization function

    # Function to print the board using the 2d array
    def printBoard(self):
        print(f"\n {self.player1.name} Scores: {self.player1.score} (Black),  {self.player2.name} Scores: {self.player2.score} (White) \n")
        print("    A    B    C    D    E    F    G    H\n")
        for i in range(SIZE):
            print(" ",end="")
            for j in range(SIZE):
                print(" ----",end="")
            print(" ")
            print(f"{i+1}",end="")
            for j in range(SIZE):
                print(f"  {self.board[i][j]}  ",end="")
            print(" ")
        for i in range(SIZE):
            print(" ----",end="")
        print(" ")
        print("    A    B    C    D    E    F    G    H\n")
        # End of printBoard function

    # Function to update the score of both players as the game progresses
    def updateScore(self):
        # Variable to hole score, set to zero
        black_scores = 0
        white_scores = 0
        for i in range(SIZE):
            for j in range(SIZE):
                if self.board[i][j] == 'B':
                    # count the number if Black on the board
                    black_scores += 1
                if self.board[i][j] == 'W':
                    # count the number if White on the board
                    white_scores += 1
        self.player1.score_update(score=black_scores)
        self.player2.score_update(score=white_scores)
        # End of updateScore function

    def validMove(self,color, drow ,dcol ,row ,col):
        opp = 'B' if color == 'W' else 'W'
        # if out of bounds, return false
        if (row + drow < 0) or (row + drow > self.size - 1) or (col + dcol < 0) or (col + dcol > self.size - 1):
            return False
        # if search reaches the same colour, return false
        if self.board[row + drow][col + dcol] != opp:
            return False
        # if two tile over in any direction of the title we're looking at is at the end of the board,
        # return false
        if (row + drow + drow) < 0 or (row + drow + drow > 7) or (col + dcol + dcol < 0) or (col + dcol + dcol > 7):
            return False
        # if not return what is gotten from the lineCheck function
        # passing the position(dRow,dCol) as the new row and col
        return self.lineCheck(color, drow, dcol, row + drow + drow, col + dcol + dcol)

    # End of validMove function

    # Function to check line
    def lineCheck(self, color, drow, dcol, row, col):
        # if the new position, the same colour tile is found,return true
        if self.board[row][col] == color:
            return True
        # if out of bounds, return false
        if (row + drow < 0) or (row + drow > self.size - 1) or (col + dcol < 0) or (
                col + dcol > self.size - 1):

            return False
        # repeat until out of bounds or colour tile is matched
        return self.lineCheck(color, drow, dcol, row + drow, col + dcol)
    def playerMove(self, color, inputs):
        row = int(inputs[1]) - 1
        col = ord(inputs[0]) - ord('a')
        self.board[row][col]=color
        opp = 'B' if color == 'W' else 'W'
        for drow in range(-1,2):
            for dcol in range(-1,2):
        # if out of bounds, skip and continue
                if (row + drow < 0) or (row + drow > self.size - 1) or (col + dcol < 0) or (col + dcol > self.size - 1) or (
                drow == 0 and dcol == 0):
                    continue
                # if tile s of opposite color
                if self.board[row + drow][col + dcol] == opp:
                    # update location
                    x = row + drow
                    y = col + dcol
                    while True:
                        # increment the location to the next along the line
                        x+=drow
                        y+=dcol
                        if x < 0 or  x > self.size - 1 or y < 0 or y > self.size - 1:
                            break
                        if self.board[x][y] == ' ':
                            break
                        if self.board[x][y] == color:
                            x -= drow
                            y -= dcol
                            while self.board[x][y] == opp:
                                x -= drow
                                y -= dcol
                            self.board[x][y] = color
                            break
        # Function to check if a slot entered by the user is a valid move
        # to be made by that player depending on their colour

    def checkMove(self, color, inputs):
        # get the row and column entered by the user
        row = int(inputs[1]) - 1
        col = ord(inputs[0]) - ord('a')
        # check in all directions using the i and j as offset positions
        for i in range(-1, 2):
            for j in range(-1, 2):
                # check if any of the directions make the move valid
                check = self.validMove(color, i, j, row, col)
                # check if any of the directions make the move valid
                if check:
                    return True
        return False

    # End of checkMove function
    def isNotEmpty(self, inputs):
        if self.board[int(inputs[1]) - 1][ord(inputs[0]) - ord('a')] == 'B':
            return True
        if self.board[int(inputs[1]) - 1][ord(inputs[0]) - ord('a')] == 'W':
            return True
        return False
# Create an othello board object
othello_board = Board()



