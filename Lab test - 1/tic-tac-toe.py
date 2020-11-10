#Implement Tic-tac-toe using a 2-agent algorithm (Computer Vs Computer)

#Board
board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]

game_still_going = True

winner = None

# Tells us who the current player is (Computer 1 or Computer 2)
current_player = "C1"

#Tells us what symbol the current player must put on the board(X or O)
current_symbol = "X"

def play_game():
  global current_player

  display_board()

  # Loop until the game stops(till someone wins or there is tie)
  while game_still_going:

    # Handle a turn
    handle_turn(current_player, current_symbol)

    # Check if the game is over
    check_if_game_over()

    # Flip to the other player
    flip_player()

    display_board()
  
  
  # If the game is over, print the final result
  
  if winner == "X":
    print("Computer 1 won")

  elif winner == None:
    print("The game ended in a tie.")
  
  else:
    print("Computer 2 won")


# Display the game board to the screen
def display_board():
  print("\n")
  print(board[0] + " | " + board[1] + " | " + board[2])
  print(board[3] + " | " + board[4] + " | " + board[5])
  print(board[6] + " | " + board[7] + " | " + board[8])
  print("\n")


# Handle a turn 
def handle_turn(player, symbol):
    print(player + "'s turn")
    w = stop_win()
    if w!= None:
      board[w] = symbol
      return
    
    w = win_is_present()
    if w != None:
      board[w] = symbol
    else:
        if board[0] == "-":
            board[0] = symbol
        elif board[2] == "-":
            board[2] = symbol
        elif board[6] == "-":
            board[6] = symbol
        elif board[8] == "-":
            board[8] = symbol
        
        else:
            for i in range(9):
                if board[i] == "-":
                    board[i] = symbol
                    break



# Check if the game is over
def check_if_game_over():
  check_for_winner()
  check_for_tie()


# Check to see if somebody has won
def check_for_winner():
  # Set global variables
  global winner
  # Check if there was a winner anywhere
  row_winner = check_rows()
  column_winner = check_columns()
  diagonal_winner = check_diagonals()
  # Get the winner
  if row_winner:
    winner = row_winner
  elif column_winner:
    winner = column_winner
  elif diagonal_winner:
    winner = diagonal_winner
  else:
    winner = None


# Check the rows for a win
def check_rows():
  global game_still_going
  row_1 = board[0] == board[1] == board[2] != "-"
  row_2 = board[3] == board[4] == board[5] != "-"
  row_3 = board[6] == board[7] == board[8] != "-"

  if row_1 or row_2 or row_3:
    game_still_going = False

  if row_1:
    return board[0] 
  elif row_2:
    return board[3] 
  elif row_3:
    return board[6] 

  else:
    return None


# Check the columns for a win
def check_columns():
  global game_still_going
  column_1 = board[0] == board[3] == board[6] != "-"
  column_2 = board[1] == board[4] == board[7] != "-"
  column_3 = board[2] == board[5] == board[8] != "-"

  if column_1 or column_2 or column_3:
    game_still_going = False

  if column_1:
    return board[0] 
  elif column_2:
    return board[1] 
  elif column_3:
    return board[2] 

  else:
    return None


# Check the diagonals for a win
def check_diagonals():

  global game_still_going
  
  diagonal_1 = board[0] == board[4] == board[8] != "-"
  diagonal_2 = board[2] == board[4] == board[6] != "-"

  if diagonal_1 or diagonal_2:
    game_still_going = False
 
  if diagonal_1:
    return board[0] 
  elif diagonal_2:
    return board[2]

  else:
    return None


# Check if there is a tie
def check_for_tie():
  # Set global variables
  global game_still_going
  #If there is nowhere to put a symbol then it is a tie
  if "-" not in board:
    game_still_going = False
    return True
  else:
    return False


# Flip the current player from C1 to C2, or C2 to C1 and also flip the current symbol
def flip_player():
  global current_player
  global current_symbol
  # If the current player was C1, make it C2 and change current symbol
  if current_player == "C1":
    current_player = "C2"
    current_symbol = 'O'
  else:
      current_player = "C1"
      current_symbol = "X"
  

#Check if you can win by marking the symbol in the right place and return the
#index of that place if present, else return none
def win_is_present():
  for i in range(9):
    if board[i] == '-':
      board[i] = current_symbol
      check_if_game_over()
      board[i] = '-'
      if not game_still_going:
        return i

#Check if the opponent can win during it's next turn. Returns the index where the
#current player must put it's symbol to stop the other computer from winning in it's next turn
def stop_win():
  flip_player()
  global game_still_going
  for i in range(9):
    if board[i] == "-":
      board[i] = current_symbol
      w = check_if_game_over()
      board[i] = "-"
      if not game_still_going:
        flip_player()
        w = check_if_game_over()
        game_still_going = True
        return i
  flip_player()
  w = check_if_game_over()

      

play_game()