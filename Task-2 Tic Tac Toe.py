import math
board = [' ' for _ in range(9)]


def print_board(board):
    for row in [board[i:i+3] for i in range(0, 9, 3)]:
        print(' | '.join(row))
        print('-' * 9)
def check_win(board, player):
    winning_combinations = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
        [0, 4, 8], [2, 4, 6]  # Diagonals
    ]

    for combo in winning_combinations:
        if all(board[combo[i]] == player for i in range(3)):
            return True
    return False
def is_board_full(board):
    return ' ' not in board
def get_empty_cells(board):
    return [i for i, cell in enumerate(board) if cell == ' ']
def minimax(board, depth, maximizing_player, alpha, beta):
    if check_win(board, 'X'):
        return -1
    if check_win(board, 'O'):
        return 1
    if is_board_full(board):
        return 0

    if maximizing_player:
        max_eval = -math.inf
        for move in get_empty_cells(board):
            board[move] = 'O'
            eval = minimax(board, depth + 1, False, alpha, beta)
            board[move] = ' '
            max_eval = max(max_eval, eval)
            alpha = max(alpha, eval)
            if beta <= alpha:
                break
        return max_eval
    else:
        min_eval = math.inf
        for move in get_empty_cells(board):
            board[move] = 'X'
            eval = minimax(board, depth + 1, True, alpha, beta)
            board[move] = ' '
            min_eval = min(min_eval, eval)
            beta = min(beta, eval)
            if beta <= alpha:
                break
        return min_eval
def best_move(board):
    best_eval = -math.inf
    best_move = None
    alpha = -math.inf
    beta = math.inf
    for move in get_empty_cells(board):
        board[move] = 'O'
        eval = minimax(board, 0, False, alpha, beta)
        board[move] = ' '
        if eval > best_eval:
            best_eval = eval
            best_move = move
    return best_move

while True:
    print_board(board)
    player_move = int(input("Enter your move (1-9): ")) - 1

    if board[player_move] == ' ':
        board[player_move] = 'X'
    else:
        print("Invalid move. Try again.")
        continue

    if check_win(board, 'X'):
        print_board(board)
        print("You win!")
        break
    elif is_board_full(board):
        print_board(board)
        print("It's a draw!")
        break

    ai_move = best_move(board)
    board[ai_move] = 'O'

    if check_win(board, 'O'):
        print_board(board)
        print("AI wins!")
        break
    elif is_board_full(board):
        print_board(board)
        print("It's a draw!")
        break