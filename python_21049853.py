import random

# List board to identify every spot for printing board
board = ["-", "-", "-", "-", "-", "-", "-", "-", "-"]  
player = "X"  # Player is always 'X'
winner = None
run_game = True

# Tell player about role of player
def introduction():
    # Tell the player that he/she is X and computer is O
    print("""WELCOME TO TIC-TAC-TOE!\n
Human(H) is 'X'            
Computer(C) is 'O'\n""")
    # To empty all record moves from the previous game
    file = open("logfile_21049853.txt", "w")  
    file.write("")
    file.close()

# Display game board and reference for user
def print_board(board):
    # Define every spot (1-9)
    print('                   Reference:')
    print(board[0] + " | " + board[1] + " | " + board[2] + '          1 | 2 | 3')  
    print("---------" + "          ---------")
    print(board[3] + " | " + board[4] + " | " + board[5] + '          4 | 5 | 6')
    print("---------" + "          ---------")
    print(board[6] + " | " + board[7] + " | " + board[8] + '          7 | 8 | 9\n')

# Take player input
def human_input(board):
    # Ask player to input a spot
    inp = int(input("Select a spot 1-9 (For example: 1): "))  
    print()
    # Record the human move and store it in logfile_21049853.txt
    file = open("logfile_21049853.txt", "a")  
    file.write(f"Human(H): X place at {inp}" + "\n")
    file.close()
    print()
    # If the particular spot is still empty("-"), the spot will placed by X
    if board[inp-1] == "-":  
        board[inp-1] = player
    # If player input a spot that already occupied by 'X' or 'O', ask the player to input again
    else:  
        print("Invalid input, this spot is occupied!\n")
        print_board(board)
        human_input(board)

# Check for row whether win or not
def check_row(board):
    # allow winner variable be used in this function
    global winner  
    if board[0] == board[1] == board[2] and board[0] != "-":  # Check for first row
        winner = board[0]
        return True
    elif board[3] == board[4] == board[5] and board[3] != "-":  # Check for second row
        winner = board[3]
        return True
    elif board[6] == board[7] == board[8] and board[6] != "-":  # Check for third row
        winner = board[6]
        return True

# Check for column whether win or not
def check_column(board):
    global winner  # allow winner variable be used in this function
    if board[0] == board[3] == board[6] and board[0] != "-":  # Check for first column
        winner = board[0]
        return True
    elif board[1] == board[4] == board[7] and board[1] != "-":  # Check for second column
        winner = board[1]
        return True
    elif board[2] == board[5] == board[8] and board[2] != "-":  # Check for third column
        winner = board[2]
        return True

# Check for diagonal whether win or not
def check_diagonal(board):
    global winner  # allow winner variable be used in this function
    if board[0] == board[4] == board[8] and board[0] != "-":
        winner = board[0]
        return True
    elif board[2] == board[4] == board[6] and board[2] != "-":
        winner = board[2]
        return True

# Check for row, column and diagonal whether win or not
def check_win(board):
    global run_game  # Allow gameRunning variable be used in this function
    if check_row(board) or check_column(board) or check_diagonal(board):
        print_board(board)
        print(f"The winner is {winner}!")  # Display who is the winner
        if winner == "X":
            print("YOU WIN!")
            print("GAME OVER!")
        elif winner == "O":
            print("YOU LOSE!")
            print("GAME OVER!")
        exit(run_game)  # Stop the game running once win

# Check for row, column and diagonal whether tie or not
def check_tie(board):
    global run_game  # Allow run_game variable be used in this function
    if "-" not in board:  # If all spots are occupied by number and '-' not exists
        print_board(board)
        print("It is a tie!")
        print("GAME OVER!")
        exit(run_game)  # Stop the game running once tie

# Switch player's turn
def switch_player():
    global player  # Allow player variable be used in this function
    if player == "X":  # If the player is X, then the next will be O
        player = "O"
    else:
        player = "X"

# Computer play
def computer(board):
    # Loop computer to place a spot
    while player == "O":  
        # Randomise a spot for computer to place
        position = random.randint(1, 9)  
        # If the particular spot is still empty, the spot will placed by O
        if board[position-1] == "-":  
            board[position-1] = "O"
            # Record the computer move and store it in logfile_21049853.txt
            file = open("logfile_21049853.txt", "a")  
            file.write(f'Computer(C): O place at {position}' + '\n')
            file.close()
            switch_player()

# Check for final result whether it is win or tie
def final_check():
    if check_win(board) is True:  # If game is win, stop the gaming process
        exit(run_game)

    elif check_tie(board) is True:  # If the game is tie, stop the gaming process
        exit(run_game)
 
# Run introduction function
introduction()

while run_game:  # Loop the whole gaming process
    # Run the whole gaming process per turn according this sequence
    print_board(board)
    human_input(board)
    final_check()
    switch_player()
    computer(board)
    final_check()





