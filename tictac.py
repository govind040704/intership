import random

# The Tic-Tac-Toe board is represented as a list of lists.
# Each element can be 'X', 'O', or ' ' (empty).
board = [[' ' for _ in range(3)] for _ in range(3)]

# Define constants for player and AI
PLAYER = 'X'
AI = 'O'

# Function to print the Tic-Tac-Toe board
def print_board(board):
    for row in board:
        print(' | '.join(row))
        print('-' * 9)

# Function to check if the board is full
def is_board_full(board):
    return all(all(cell != ' ' for cell in row) for row in board)

# Function to check if the current player has won
def is_winner(board, player):
    # Check rows, columns, and diagonals
    for i in range(3):
        if all(board[i][j] == player for j in range(3)) or \
           all(board[j][i] == player for j in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)) or \
       all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

# Function to evaluate the current state of the board
def evaluate(board):
    if is_winner(board, AI):
        return 1
    if is_winner(board, PLAYER):
        return -1
    return 0

# Minimax function with Alpha-Beta Pruning
def minimax(board, depth, maximizing_player, alpha, beta):
    if is_winner(board, AI):
        return 1
    if is_winner(board, PLAYER):
        return -1
    if is_board_full(board):
        return 0

    if maximizing_player:
        max_eval = float('-inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = AI
                    eval = minimax(board, depth + 1, False, alpha, beta)
                    board[i][j] = ' '
                    max_eval = max(max_eval, eval)
                    alpha = max(alpha, eval)
                    if beta <= alpha:
                        break
        return max_eval
    else:
        min_eval = float('inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = PLAYER
                    eval = minimax(board, depth + 1, True, alpha, beta)
                    board[i][j] = ' '
                    min_eval = min(min_eval, eval)
                    beta = min(beta, eval)
                    if beta <= alpha:
                        break
        return min_eval

# Function to find the best move for the AI player
def best_move(board):
    best_eval = float('-inf')
    best_move = None
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                board[i][j] = AI
                eval = minimax(board, 0, False, float('-inf'), float('inf'))
                board[i][j] = ' '
                if eval > best_eval:
                    best_eval = eval
                    best_move = (i, j)
    return best_move

# Main game loop
while True:
    print_board(board)
    
    # Player's turn
    while True:
        try:
            row, col = map(int, input("Enter your move (row[0-2] and column[0-2] separated by space): ").split())
            if board[row][col] == ' ':
                board[row][col] = PLAYER
                break
            else:
                print("Invalid move. Try again.")
        except (ValueError, IndexError):
            print("Invalid input. Please enter valid row and column values.")

    # Check if player wins
    if is_winner(board, PLAYER):
        print_board(board)
        print("Congratulations! You win!")
        break
    
    # Check if the board is full (draw)
    if is_board_full(board):
        print_board(board)
        print("It's a draw!")
        break

    # AI's turn
    print("AI's turn:")
    row, col = best_move(board)
    board[row][col] = AI

    # Check if AI wins
    if is_winner(board, AI):
        print_board(board)
        print("AI wins! Better luck next time.")
        break

    # Check if the board is full (draw)
    if is_board_full(board):
        print_board(board)
        print("It's a draw!")
        break
