def print_board(board):
    for row in board:
        print("|".join(row))
        print("-" * 5)

def check_winner(board):
    # Check rows and columns
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != ' ':
            return board[i][0], True
        if board[0][i] == board[1][i] == board[2][i] != ' ':
            return board[0][i], True

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] != ' ':
        return board[0][0], True
    if board[0][2] == board[1][1] == board[2][0] != ' ':
        return board[0][2], True

    return None, False

def is_board_full(board):
    for row in board:
        if ' ' in row:
            return False
    return True

def main():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    player = 'X'

    while True:
        print_board(board)

        row = int(input(f"Enter the row (0, 1, or 2) for {player}: "))
        col = int(input(f"Enter the column (0, 1, or 2) for {player}: "))

        if board[row][col] == ' ':
            board[row][col] = player
        else:
            print("Cell already taken. Try again.")
            continue

        winner, is_game_over = check_winner(board)
        if is_game_over:
            print_board(board)
            print(f"Player {winner} wins!")
            break

        if is_board_full(board):
            print_board(board)
            print("It's a tie!")
            break

        player = 'O' if player == 'X' else 'X'

if __name__ == "__main__":
    main()
