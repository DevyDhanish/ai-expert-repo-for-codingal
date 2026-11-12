# make a tic tac toe game



board = [" " for _ in range(9)]

def display_board():
    print()
    for i in range(0, 9, 3):
        print(" " + " | ".join(board[i:i+3]))
        if i < 6:
            print("---+---+---")
    print()

def check_winner():
    winning_positions = [
        (0, 1, 2), (3, 4, 5),
        (0, 3, 6), (1, 4, 7),
        (2, 5, 8), (6, 7, 8),
        (0, 4, 8), (2, 4, 6)
    ]

    for a, b, c in winning_positions:
        if board[a] == board[b] == board[c] != " ":
            return board[a]

    return None

def play_game():
    current_player = "X"

    while True:
        display_board()

        try:
            position = int(input(
                f"Player {current_player}, choose position (1-9): "
            )) - 1

            if position < 0 or position > 8:
                print("Invalid position!")
                continue

            if board[position] != " ":
                print("That position is already occupied!")
                continue

        except ValueError:
            print("Please enter a valid number!")
            continue

        board[position] = current_player

        winner = check_winner()

        if winner:
            display_board()
            print(f"Player {winner} wins! 🎉")
            break

        if " " not in board:
            display_board()
            print("It's a draw!")
            break

        current_player = "O" if current_player == "X" else "X"


play_game()
