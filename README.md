# Tic-Tac-Toe with AI

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green)](LICENSE)

A console-based implementation of Tic-Tac-Toe featuring an unbeatable AI opponent using the Minimax algorithm with Alpha-Beta pruning and memoization optimization.

## Features

- 🎮 Play against an unbeatable AI on 3x3 boards
- ⚙️ Support for custom board sizes (4x4, 5x5, etc.)
- ⚡ Optimized performance with memoization caching
- 📊 Detailed game statistics and move analysis
- 🖥️ Simple console interface with easy controls

## How It Works

The AI uses sophisticated algorithms to make optimal moves:

- **Minimax Algorithm**: Evaluates all possible future game states
- **Alpha-Beta Pruning**: Dramatically reduces computation time by eliminating unpromising branches
- **Memoization**: Caches game states to avoid redundant calculations

### Performance Optimization

| Board Size | States | Without Memoization | With Memoization |
|------------|--------|---------------------|------------------|
| 3x3        | ~9!    | 100 ms              | 1 ms            |
| 4x4        | ~16!   | >10 minutes         | 20 seconds      |
| 5x5        | ~25!   | >1 hour             | ~60 minutes      |

## Installation

1. Clone the repository:
```bash
git clone https://github.com/Sandraiffa1/tik-toe/tree/main
cd tik-toe
```

2. Run the game:
```bash
python tik_toe.py
```

## How to Play

1. Enter the board size when prompted (3 for classic game)
2. On your turn, enter your move as row and column numbers (0-based index)
3. Watch as the AI calculates and makes its optimal move

Example game:
```
Enter board size: 3
 | | 
-----
 | | 
-----
 | | 

Your move (row col): 1 1

 | | 
-----
 |X| 
-----
 | | 

AI is thinking...
AI plays 0 0
O| | 
-----
 |X| 
-----
 | | 
```

## Technical Details

### Key Algorithms

- **Minimax with Alpha-Beta Pruning**:
  ```python
  def alpha_beta(self, depth, alpha, beta, maximizing_player):
      # Alpha-beta pruning implementation
      ...
  ```

- **Memoization Optimization**:
  ```python
  def board_to_tuple(self):
      return tuple(tuple(row) for row in self.board)
  
  if board_key in self.memo:  # Check cache
      return self.memo[board_key]
  ```

### Project Structure

- `tik_toe.py` - Main game implementation
  - `TicTacToe` class - Core game logic
  - `alpha_beta()` - AI decision algorithm
  - `best_move()` - Selects optimal AI move
  - `play()` - Main game loop

## Future Improvements

- [ ] Implement GUI using PyGame
- [ ] Improved heuristics for larger boards

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any:
- Bug fixes
- Performance improvements
- New features
- Documentation enhancements
