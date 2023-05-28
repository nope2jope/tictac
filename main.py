import random

board = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
rows = 3
columns = 3
player_x = "X"

for i in range(len(board)):
    print(board[i])

player_choice = int(input("Choose a space"))
print(player_choice)


def check_choice(loc):
    if loc == "X" or loc == "O":
        print("Space already chosen!")
        return False
    else:
        return True


def mark_board(choice, player):
    if choice == 1:
        board[0][0] = player
    elif choice == 2:
        board[0][1] = player
    elif choice == 3:
        board[0][2] = player
    elif choice == 4:
        board[1][0] = player
    elif choice == 5:
        board[1][1] = player
    elif choice == 6:
        board[1][2] = player
    elif choice == 7:
        board[2][0] = player
    elif choice == 8:
        board[2][1] = player
    elif choice == 9:
        board[2][2] = player

if check_choice(loc=player_choice) == True:
    mark_board(choice=player_choice, player=player_x)

for i in range(len(board)):
    print(board[i])
