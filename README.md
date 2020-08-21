# SudokuSolver

## Solving Suduko Puzzles in Python with Backtracking ##

**Input Format:**

The Sudoku Board is currently hard-coded into the script. The format is a list called **board** containing nine additional lists. The elements of the lists internal to **board** are integers ranging from 0 through 9 where zeros represent the unsolved/empty squares of the puzzle.

```python
board = [
    [5,3,0,0,7,0,0,0,0],
    [6,0,0,1,9,5,0,0,0],
    [0,9,8,0,0,0,0,6,0],
    [8,0,0,0,6,0,0,0,3],
    [4,0,0,8,0,3,0,0,1],
    [7,0,0,0,2,0,0,0,6],
    [0,6,0,0,0,0,2,8,0],
    [0,0,0,4,1,9,0,0,5],
    [0,0,0,0,8,0,0,7,9]
]
```

The value of board can be modified to represent any valid Sudoku puzzle and, when run, will print out the unsolved board followed by the solved board.

## Future

This script was written as a personal challenge. There are no current plans to extend it, however it may eventually see use in an OCR project meant to work with screenshots or cell phone cameras. Only time will tell.
