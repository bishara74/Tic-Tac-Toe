def print_board(board):
    for i in range(3):
        print(" | ".join(board[i]))
        if i != 2:
            print("-" * 9)

def check_winner(board):
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != " ":
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] != " ":
            return board[0][i]
    if board[0][0] == board[1][1] == board[2][2] != " ":
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != " ":
        return board[0][2]
    return None

board = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
players = ["X", "O"]
turn = 0

print("Welcome to Tic Tac Toe!")
print_board(board)

while True:
    player = players[turn % 2]
    row = int(input("Player " + player + ", enter row (1-3): ")) - 1
    col = int(input("Player " + player + ", enter column (1-3): ")) - 1
    if board[row][col] != " ":
        print("Invalid move. Please try again.")
        continue
    board[row][col] = player
    print_board(board)
    winner = check_winner(board)
    if winner is not None:
        print("Player", winner, "wins!")
        break
    turn += 1
    if turn == 9:
        print("It's a tie!")
        break
