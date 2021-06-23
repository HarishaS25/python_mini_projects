# solving sudoku using back tracking process
def is_sudoku_solved(matrix: list) -> bool:
    for i in range(9):
        for j in range(9):
            if matrix[i][j] == -1:
                return False
    return True


def empty_cell_pos(matrix: list):
    for i in range(9):
        for j in range(9):
            if matrix[i][j] == -1:
                return i, j
    return None, None


def check_guess(matrix, row, col, value):
    for i in range(9):
        if matrix[row][i] == value:
            return False
        if matrix[i][col] == value:
            return False
    square_row_start = row // 3 * 3
    square_col_start = col // 3 * 3
    for i in range(3):
        for j in range(3):
            if matrix[square_row_start + i][square_col_start + j] == value:
                return False
    return True


def sudoku_solver(matrix: list) -> bool:
    row, col = empty_cell_pos(matrix)
    if row is None:
        return True
    for guess in range(1, 10):
        if check_guess(matrix, row, col, guess):
            matrix[row][col] = guess
            if sudoku_solver(matrix):
                return True
            matrix[row][col] = -1

    return False


example_board = [
    [3, 9, -1, -1, 5, -1, -1, -1, -1],
    [-1, -1, -1, 2, -1, -1, -1, -1, 5],
    [-1, -1, -1, 7, 1, 9, -1, 8, -1],
    [-1, 5, -1, -1, 6, 8, -1, -1, -1],
    [2, -1, 6, -1, -1, 3, -1, -1, -1],
    [-1, -1, -1, -1, -1, -1, -1, -1, 4],
    [5, -1, -1, -1, -1, -1, -1, -1, -1],
    [6, 7, -1, 1, -1, 5, -1, 4, -1],
    [1, -1, 9, -1, -1, -1, 2, -1, -1]
]

if sudoku_solver(example_board):
    for i in range(9):
        for j in range(9):
            print(example_board[i][j], end=" ")
        print()
else:
    print("Invalid sudoku")
