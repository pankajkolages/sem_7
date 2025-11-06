# ---------------------------------------------------------------
# Program: N-Queens Problem using Backtracking
# Description:
#   This program solves the N-Queens problem for any N x N chessboard.
#   It can optionally accept the position of the first queen (row and column)
#   and then uses backtracking to place the remaining queens so that
#   no two queens attack each other.
#
# Author: Pankaj Kolage (DAA Practical)
# ---------------------------------------------------------------


def is_safe_position(chess_board, current_row, current_col):
    """
    Function to check if a queen can be safely placed
    in chess_board[current_row][current_col].

    A position is safe if:
      1. No queen exists in the same column.
      2. No queen exists in the same diagonal.
    """
    board_size = len(chess_board)

    for row_index in range(board_size):
        if row_index == current_row:
            continue  # Skip checking the current row itself

        queen_col = chess_board[row_index]  # Column of queen in this row

        if queen_col == -1:
            continue  # No queen placed in this row yet

        # Check for same column attack
        if queen_col == current_col:
            return False

        # Check for diagonal attack
        if abs(queen_col - current_col) == abs(row_index - current_row):
            return False

    return True  # Safe position


def solve_n_queens(chess_board, start_row=0):
    """
    Recursive function to place queens on the board using backtracking.

    Parameters:
      chess_board : list where index = row and value = column of queen
      start_row   : row from where to start placing queens

    Returns:
      True  -> if a valid configuration is found
      False -> if no configuration is possible
    """
    board_size = len(chess_board)

    # Find next empty row (one that doesn't have a queen yet)
    current_row = start_row
    while current_row < board_size and chess_board[current_row] != -1:
        current_row += 1

    # Base case: all rows are filled with queens
    if current_row == board_size:
        return True

    # Try placing queen in each column for this row
    for current_col in range(board_size):
        if is_safe_position(chess_board, current_row, current_col):
            chess_board[current_row] = current_col  # Place queen

            # Recursive call for next row
            if solve_n_queens(chess_board, current_row + 1):
                return True  # Found valid configuration

            # Backtrack if placing here doesn't lead to solution
            chess_board[current_row] = -1

    # No valid position in this row → backtrack
    return False


def display_chess_board(chess_board):
    """
    Function to display the chess board in a human-readable format.
    'Q' represents a queen.
    '.' represents an empty cell.
    """
    board_size = len(chess_board)
    for row_index in range(board_size):
        print(" ".join('Q' if chess_board[row_index] == col_index else '.'
                       for col_index in range(board_size)))
    print()


def n_queens_with_first_placement(board_size, first_row=-1, first_col=-1):
    """
    Function to solve the N-Queens problem with an optional
    pre-placed first queen.

    Parameters:
      board_size : size of the chessboard (N)
      first_row  : row index of first queen (-1 if not pre-placed)
      first_col  : column index of first queen (-1 if not pre-placed)
    """
    # Initialize board: -1 means no queen placed yet
    chess_board = [-1] * board_size

    # Place first queen if provided
    if first_row != -1 and first_col != -1:
        # Validate range of input coordinates
        if not (0 <= first_row < board_size and 0 <= first_col < board_size):
            print(" Error: First queen coordinates are out of range!")
            return

        chess_board[first_row] = first_col

        # Validate if the first queen placement is safe
        if not is_safe_position(chess_board, first_row, first_col):
            print(" Error: The pre-placed queen position is invalid.")
            return

    # Solve the N-Queens problem using backtracking
    if solve_n_queens(chess_board, 0):
        print(f"\n One valid {board_size}-Queens solution "
              f"(respecting pre-placed queen):")
        display_chess_board(chess_board)
    else:
        print(" No valid solution exists for this configuration.")


if __name__ == "__main__":
    print("N-Queens Problem using Backtracking")
    board_size = int(input("Enter the size of the board (e.g., 8): "))

    first_row_input = int(input("Enter the row index of the first queen (0-indexed), or -1 to skip: "))

    first_col_input = -1
    if first_row_input != -1:
        first_col_input = int(input("Enter the column index of the first queen (0-indexed): "))

    n_queens_with_first_placement(board_size,
                                  first_row=first_row_input,
                                  first_col=first_col_input)


# | Type      | Complexity | Description                                             |
# | --------- | ---------- | ------------------------------------------------------- |
# | **Time**  | O(N!)      | Because we explore all combinations of queen placements |
# | **Space** | O(N²)**    | To store the board and recursive calls                  |


# | Question                                           | Answer                                                               |
# | -------------------------------------------------- | -------------------------------------------------------------------- |
# | What does backtracking mean?                       | Trying possible options and undoing them if they lead to a dead end. |
# | What is the constraint in N-Queens problem?        | No two queens can be in the same row, column, or diagonal.           |
# | What is the base case in your recursive function?  | When `row == N`, meaning all queens are placed safely.               |
# | What is the size of the solution space?            | N! (since one queen per row).                                        |
# | Can the first queen’s position affect solvability? | Yes, some starting positions have no valid complete solution.        |
