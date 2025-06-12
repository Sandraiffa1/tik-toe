import sys
import math


class TicTacToe:
    def __init__(self, size=3):
        """Initialize the Tic-Tac-Toe board of given size."""
        self.size = size
        self.board = [[' ' for _ in range(size)] for _ in range(size)]
        self.current_player = 'X'
        self.memo = {}  # словарь для memoization

    def display_board(self):
        """Display the current board state."""
        for row in self.board:
            print('|'.join(row))
            print('-' * (self.size * 2 - 1))

    def make_move(self, row, col, player):
        """Make a move on the board."""
        if self.board[row][col] == ' ':
            self.board[row][col] = player
            return True
        return False

    def undo_move(self, row, col):
        """Undo the last move made on the board."""
        self.board[row][col] = ' '

    def is_winner(self, player):
        """Check if the specified player has won."""
        # Check rows, columns, and diagonals for a win
        for row in range(self.size):
            if all(self.board[row][col] == player for col in range(self.size)):
                return True
        for col in range(self.size):
            if all(self.board[row][col] == player for row in range(self.size)):
                return True
        if all(self.board[i][i] == player for i in range(self.size)):
            return True
        if all(self.board[i][self.size - 1 - i] == player for i in range(self.size)):
            return True
        return False

    def is_full(self):
        """Check if the board is full."""
        return all(self.board[row][col] != ' ' for row in range(self.size) for col in range(self.size))

    def board_to_tuple(self):
        return tuple(tuple(row) for row in self.board)

    def alpha_beta(self, depth, alpha, beta, maximizing_player):
        board_key = self.board_to_tuple()
        if board_key in self.memo:
            return self.memo[board_key]

        if self.is_winner('X'):
            return -10 + depth
        if self.is_winner('O'):
            return 10 - depth
        if self.is_full():
            return 0

        if maximizing_player:
            max_eval = -math.inf
            for row in range(self.size):
                for col in range(self.size):
                    if self.board[row][col] == ' ':
                        self.make_move(row, col, 'O')
                        eval = self.alpha_beta(depth + 1, alpha, beta, False)
                        self.undo_move(row, col)
                        max_eval = max(max_eval, eval)
                        alpha = max(alpha, eval)
                        if beta <= alpha:
                            break
            self.memo[board_key] = max_eval
            return max_eval
        else:
            min_eval = math.inf
            for row in range(self.size):
                for col in range(self.size):
                    if self.board[row][col] == ' ':
                        self.make_move(row, col, 'X')
                        eval = self.alpha_beta(depth + 1, alpha, beta, True)
                        self.undo_move(row, col)
                        min_eval = min(min_eval, eval)
                        beta = min(beta, eval)
                        if beta <= alpha:
                            break
            self.memo[board_key] = min_eval
            return min_eval

    def best_move(self):
        """Find the best move for the AI (O) using the Alpha-Beta pruning algorithm."""
        best_score = -math.inf
        move = None
        for row in range(self.size):
            for col in range(self.size):
                if self.board[row][col] == ' ':
                    self.make_move(row, col, 'O')
                    score = self.alpha_beta(0, -math.inf, math.inf, False)
                    self.undo_move(row, col)
                    if score > best_score:
                        best_score = score
                        move = (row, col)
        return move

    def play(self):
        """Play the game."""
        while True:
            self.display_board()
            if self.current_player == 'X':  # ход игрока
                try:
                    row, col = map(int, input("Enter your move (row and column): ").split())
                except ValueError:
                    print("Invalid input format! Enter two integers separated by space.")
                    continue

                if row < 0 or row >= self.size or col < 0 or col >= self.size:
                    print(f"Invalid move! Please enter values between 0 and {self.size-1}.")
                    continue

                if not self.make_move(row, col, 'X'):
                    print("Invalid move! Try again.")
                    continue
            else:  # AI's turn
                move = self.best_move()
                if move is not None:
                    self.make_move(move[0], move[1], 'O')
                    print(f"AI plays {move[0]} {move[1]}")

            if self.is_winner(self.current_player):
                print(f"{self.current_player} wins!")
                self.display_board()
                break

            if self.is_full():
                print("It's a tie!")
                self.display_board()
                break

            self.current_player = 'O' if self.current_player == 'X' else 'X'


if __name__ == "__main__":
    size = int(input("Enter the size of the Tic-Tac-Toe board (3 or greater): "))
    game = TicTacToe(size=size)
    game.play()
