# Define the initial state of the board as a 3x3 list of empty spaces
board = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "]
]

# Define a variable to keep track of the current player
current_player = "X"

# Define a function to print the current state of the board
def print_board():
    print("  1   2   3")
    print("1 {} | {} | {}".format(board[0][0], board[0][1], board[0][2]))
    print(" ---+---+---")
    print("2 {} | {} | {}".format(board[1][0], board[1][1], board[1][2]))
    print(" ---+---+---")
    print("3 {} | {} | {}".format(board[2][0], board[2][1], board[2][2]))

# Define a function to check if a player has won
def is_winner(player):
    # Check horizontal lines
    for row in board:
        if row == [player, player, player]:
            return True
    # Check vertical lines
    for col in range(3):
        if board[0][col] == player and board[1][col] == player and board[2][col] == player:
            return True
    # Check diagonal lines
    if board[0][0] == player and board[1][1] == player and board[2][2] == player:
        return True
    if board[0][2] == player and board[1][1] == player and board[2][0] == player:
        return True
    return False

# Define a function to ask the current player for their move
def get_move():
    while True:
        move = input("Enter row,column (e.g. 1,1 for top-left): ")
        try:
            row, col = move.split(",")
            row = int(row) - 1
            col = int(col) - 1
        except ValueError:
            print("Invalid input. Please enter row,column (e.g. 1,1 for top-left).")
            continue
        if row < 0 or row > 2 or col < 0 or col > 2:
            print("Invalid input. Please enter a row and column between 1 and 3.")
            continue
        if board[row][col] != " ":
            print("That spot is already taken. Please choose another spot.")
            continue
        return row, col

# Define the main game loop
while True:
    # Print the current state of the board
    print_board()
    # Ask the current player for their move
    print("It's", current_player, "'s turn.")
    row, col = get_move()
    # Update the board with the current player's move
    board[row][col] = current_player
    # Check if the current player has won
    if is_winner(current_player):
        print_board()
        print(current_player, "wins!")
        break
    # Check if the game has ended in a tie
    if all(" " not in row for row in board):
        print_board()
        print("Tie game!")
        break
    # Switch to the other player
    current_player = "O" if current_player == "X" else "X"