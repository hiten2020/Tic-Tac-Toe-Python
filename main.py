# Tic-Tac-Toe using pyhton


# ****Divide task ****

# board
# display board
# play game
# handleturn
# check win
  # check row
  # check column
  # chek diagonals

# check tie
# flip player

# GLOBAL variables


board = ["-","-","-",
        "-","-","-",
        "-","-","-"]

# Tf game is still game_still_going
game_still_going = True

# Who won ? Or tie?
winner  = None

# whos turn is it?
current_player = "X"



def display_board():
  print(board[0] + "|" + board[1]+"|"+board[2])
  print(board[3] + "|" + board[4]+"|"+board[5])
  print(board[6] + "|" + board[7]+"|"+board[8])


def handle_turn(current_player):

    print(current_player + "'S turn")

    position = input("Choose a position from 1-9 ")

    while position not in ["1","2","3","4","5","6","7","8","9"]:
        position = input("Invalid input, Choose a position from 1-9")

    position = int(position)-1
    if board[position]!="-":
        print("You can't go there. Go again")
    board[position]=current_player
    display_board()

  

def check_rows():
    # set up global variable
    global game_still_going
    # check if any rows have all the same value
    row_1 = board[0]==board[1]==board[2] !="-"
    row_2 = board[3]==board[4]==board[5] !="-"
    row_3 = board[6]==board[7]==board[8] !="-"

    if row_1 or row_2 or row_3:
        game_still_going=False
    
    # Return the winner
    if row_1:
        return board[0]
    elif row_2:
        return board[3]
    elif row_3:
        return board[6]
    return

def check_columns():
    # set up global variable
    global game_still_going
    # check if any columns have all the same value
    column_1 = board[0]==board[3]==board[6] !="-"
    column_2 = board[1]==board[4]==board[7] !="-"
    column_3 = board[2]==board[5]==board[8] !="-"

    if column_1 or column_2 or column_3:
        game_still_going=False
    
    # Return the winner
    if column_1:
        return board[0]
    elif column_2:
        return board[1]
    elif column_3:
        return board[2]
    return


def check_diagonals():
    # set up global variable
    global game_still_going
    # check if any diagonals have all the same value
    diagonal_1 = board[0]==board[4]==board[8] !="-"
    diagonal_2 = board[2]==board[4]==board[6] !="-"

    if diagonal_1 or diagonal_2 :
        game_still_going=False
    
    # Return the winner
    if diagonal_1:
        return board[0]
    elif diagonal_2:
        return board[2]

    return

def check_if_win():
    # set up global variable
    global winner
    # check rows
    row_winner = check_rows()
    # check columns
    column_winner = check_columns()
    # check diagonals
    diagonal_winner = check_diagonals()

    if row_winner:
        winner = row_winner
    elif column_winner:
        winner = column_winner
    elif diagonal_winner:
        winner = diagonal_winner
    else:
        winner = None

def check_if_tie():
    global game_still_going
    if "-" not in board:
        game_still_going = False
    return

def check_if_game_over():
    check_if_tie()
    check_if_win()

def flip_player():
    global current_player

    if current_player=="X":
        current_player="O"
    elif current_player=="O":
        current_player="X"

# Play game tic-tac-toe
def play_game():
    display_board()

    
    while game_still_going:

        # handle a single turn arbitrary player
        handle_turn(current_player)

        # check if game has ended
        check_if_game_over()

        # flip to other player
        flip_player()

    #The game is ended
    if winner=="X" or winner=="O":
        print(winner + " won.")
    elif winner==None:
        print("Tie.")


play_game()