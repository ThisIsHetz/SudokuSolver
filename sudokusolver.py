# sudokusolver.py
# Let's solve sudokus

# excessive comments intentionally left in
# for the benefit of both the author and
# the observer

# the sudoku board is constructed in the form
# of a list of nine lists, representing the
# 9 by 9 grid. Existing numbers are filled
# in while the blank spaces meant to be solved
# are represented by zeros

board = [
    [5,3,0,0,7,0,0,0,0],
    [6,0,0,1,9,5,0,0,0],
    [0,9,8,0,0,0,0,6,0],
    [8,0,0,0,6,0,0,0,3],
    [4,0,0,8,0,3,0,0,1],
    [7,0,0,0,2,0,0,0,6],
    [0,6,0,0,0,0,2,8,0],
    [0,0,0,4,1,9,0,0,5],
    [0,0,0,0,8,0,0,7,9]]


# this function examines the lists locating the first
# instance of a zero (meaning a blank/unsolved square)
# are returning the "row" and "column."
# Rows can be thought of as the individual lists within
# the board list, columns are the specific index within
# a particular list.

def isEmpty(board):
    for row in range(len(board)):
        for col in range(len(board[0])):
            if board[row][col] == 0:
                return row, col


 # this function is called inside the solve() function
 # to check if a current number (num) is a valid entry
 # into a blank square. if num is present in either
 # the row, column or 3x3 square the current row/column
 # coordinates reside in, it would violate the rules of
 # sudoku to place the duplicate number in the blank
 # square.

def isValid(board, num, row, col):
    # Checking the row
    if num in board[row]:
        return False

    # Checking the column
    for r in range(len(board)):
        if board[r][col] == num:
            return False
    
    # Check the square
    # Below is a neat use of floored division which
    # returns only how many times a number can be
    # cleanly divided by another, ignoring any
    # remainder.

    # For example 7 // 3 = 2
    # because three can only go into seven twice (six)
    # with an ignored remainder of 1

    # Specific to solving sudokos:
    # 0, 1, or 2 // 3 = 0
    # 3, 4, or 5 // 3 = 1
    # 6, 7, or 8 // 3 = 2
    # Multiplied by 3 we get 0, 3, and 6

    # This allows us to get the top-left coordinates
    # for whichever of the nine 3 by 3 boxes the
    # current row, col coordinates reside. We can
    # then go through that box checking if our current
    # number being attempted is already present.

    box_y = (row // 3) * 3
    box_x = (col // 3) * 3

    for r in range(box_y, box_y+3):
        for c in range(box_x, box_x+3):
            if board[r][c] == num:
                return False
    
    else:
        return True


# Our recursive solve() function
def solve(board):
    # Use isEmpty() to assign coordinates to spot.
    # If nothing gets assigned to spot return
    # True because the puzzle is solved
    spot = isEmpty(board)
    if not spot:
        return True
    
    # If not solved, use spot to set the row
    # and column values to pass along to the
    # isValid() function.
    else:
        row, col = spot

    # The magic happens below.
    # solve(board) gets called within itself
    # with each currently valid entry at
    # row, col.

    # If after num progresses from 1 through 9
    # and no valid entry can be made, the value
    # at row, col is set back to zero and the
    # current recurrance of solve() ends, falling
    # back to the previous call of solve() and the
    # previous call of isValid() with the value of
    # num progressing.

    for num in range(1, 10):
        if isValid(board, num, row, col):
            board[row][col] = num

            if solve(board):
                return True
            
            board[row][col]=0

    return False

# an ugly little print function to display the
# board before and after solve() has been called

def print_board(board):
    for i in range(len(board)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - -")

        for j in range(len(board[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")

            if j == 8:
                if board[i][j] == 0:
                    print(" ")
                else:
                    print(board[i][j])
            else:
                if board[i][j] == 0:
                    print(" " + " ", end="")
                else:
                    print(str(board[i][j]) + " ", end="")


print_board(board)
print("\n")
solve(board)
print_board(board)