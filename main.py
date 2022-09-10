from gameplay import Gameplay
from datetime import datetime

othello_game=Gameplay()
othello_game.initiliaseGameplay()

player1_name=input("Please input name:")
othello_game.player1.name_update(name=player1_name)

player2_name=input("Please input name:")
othello_game.player2.name_update(name=player2_name)

othello_game.board.printBoard()
print(f'{othello_game.player1.name} goes first')

while othello_game.numOfTiles != othello_game.board.size*othello_game.board.size:
    if othello_game.movesAvilable(othello_game.player1):
        othello_game.playPlayers(othello_game.player1)
    if othello_game.movesAvilable(othello_game.player2):
        othello_game.playPlayers(othello_game.player2)
    if (not othello_game.movesAvilable(othello_game.player1)) and (not othello_game.movesAvilable(othello_game.player2)):
        break

print("Game over \n")

if othello_game.player1.score > othello_game.player2.score:
    print(f'{othello_game.player1.name} wins!!!')
elif othello_game.player2.score > othello_game.player1.score:
    print(f'{othello_game.player2.name} wins!!!')
else:
    print("It a tie!!!")
try:
    with open("Othello Results", mode='a') as file:
        file.write(f"Game played on {datetime.now()} \n")
        file.write(f"{othello_game.player1.name}: Score:{othello_game.player1.score}\n"
                   f"{othello_game.player2.name}: Score:{othello_game.player2.score}\n")
except FileNotFoundError:
    with open("Othello Results", mode='w') as file:
        file.write(f"Game played on {datetime.now()} \n")
        file.write(f"{othello_game.player1.name}: Score:{othello_game.player1.score}\n"
                   f"{othello_game.player2.name}: Score:{othello_game.player2.score}\n")


