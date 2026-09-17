def print_board(board):
    print()
    print(" " + board[0] + " | " + board[1] + " | " + board[2])
    print("---+---+---")
    print(" " + board[3] + " | " + board[4] + " | " + board[5])
    print("---+---+---")
    print(" " + board[6] + " | " + board[7] + " | " + board[8])
    print()


def check_winner(board, player):
    winning_combinations = [
        (0, 1, 2),
        (3, 4, 5),
        (6, 7, 8),
        (0, 3, 6),
        (1, 4, 7),
        (2, 5, 8),
        (0, 4, 8),
        (2, 4, 6)
    ]

    for a, b, c in winning_combinations:
        if board[a] == player and board[b] == player and board[c] == player:
            return True

    return False


def check_draw(board):
    return all(position != " " for position in board)


def play_game():
    board = [" "] * 9
    current_player = "X"

    while True:
        print_board(board)

        print("Player", current_player, "turn")

        try:
            position = int(input("Enter position (1-9): ")) - 1
        except ValueError:
            print("Please enter a valid number.")
            continue

        if position < 0 or position > 8:
            print("Position must be between 1 and 9.")
            continue

        if board[position] != " ":
            print("This position is already occupied.")
            continue

        board[position] = current_player

        if check_winner(board, current_player):
            print_board(board)
            print("Player", current_player, "wins!")
            break

        if check_draw(board):
            print_board(board)
            print("The game is a draw!")
            break

        if current_player == "X":
            current_player = "O"
        else:
            current_player = "X"


print("===== TIC TAC TOE =====")
print("Positions are numbered from 1 to 9.")

play_game()

