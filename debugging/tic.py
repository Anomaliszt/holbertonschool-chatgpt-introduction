def print_board(board):
    """
    Prints the current state of the board.
    """
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(board):
    """
    Checks if there is a winner on the board.
    
    Returns:
    True if there is a winner, otherwise False.
    """
    # Check rows
    for row in board:
        if row.count(row[0]) == len(row) and row[0] != " ":
            return True

    # Check columns
    for col in range(len(board)):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != " ":
            return True

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return True
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return True

    return False

def tic_tac_toe():
    """
    Main function to play the Tic Tac Toe game.
    """
    board = [[" " for _ in range(3)] for _ in range(3)]
    player = "X"
    
    for _ in range(9):  # Maximum 9 moves
        print_board(board)
        while True:
            try:
                row = int(input(f"Enter row (0, 1, or 2) for player {player}: "))
                col = int(input(f"Enter column (0, 1, or 2) for player {player}: "))
                if row not in [0, 1, 2] or col not in [0, 1, 2]:
                    print("Invalid input. Please enter 0, 1, or 2 for row and column.")
                    continue
                if board[row][col] != " ":
                    print("That spot is already taken! Try again.")
                else:
                    break
            except ValueError:
                print("Invalid input. Please enter numeric values.")

        board[row][col] = player
        if check_winner(board):
            print_board(board)
            print(f"Player {player} wins!")
            return
        
        player = "O" if player == "X" else "X"

    print_board(board)
    print("It's a tie!")

tic_tac_toe()
