# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

def is_solved(board):
    """
    Takes in 2D List as a sudoku board
    Returns whether the sudoku board is solved
    """
    solved = True
    col_lst = [set() for i in range(9)]
    box_lst = [set() for i in range(9)]
    box_inc = -1

    # Looping through the integers in the 2D List
    for row in range(len(board)):

        # If the row does not have 9 unique numbers the board isn't solved
        tmp_row = set(board[row])
        if len(tmp_row) != 9:
            solved = False
            break

        for col in range(len(board)):

            # If there are empty spots the board isn't solved
            if board[row][col] == 0:
                solved = False
                break

            # Adds to the set in the list to check for unique numbers later
            col_lst[col].add(board[row][col])

            # Increments so that sets of the box values can be checked later
            if col % 3 == 0:
                box_inc += 1
            if col == 0:
                if row % 3 == 0:
                    pass
                else:
                    box_inc -= 3

            box_lst[box_inc].add(board[row][col])

        # Exits outer loop upon break
        else:
            continue
        break

    # Evaluates column sets and box sets
    if solved:

        for col in col_lst:
            if len(col) != 9:
                solved = False

        for box in box_lst:
            if len(box) != 9:
                solved = False

    return solved

def solve(board):
    pass



puzzle = [
    [6, 0, 0, 0, 0, 5, 1, 0, 0],
    [8, 0, 2, 0, 0, 0, 0, 9, 0],
    [0, 0, 0, 0, 1, 4, 0, 0, 0],
    [1, 0, 6, 3, 0, 0, 0, 5, 0],
    [2, 0, 0, 0, 0, 0, 0, 0, 1],
    [0, 5, 0, 0, 0, 1, 7, 0, 3],
    [0, 0, 0, 7, 8, 0, 0, 0, 0],
    [0, 9, 0, 0, 0, 0, 5, 0, 2],
    [0, 0, 4, 5, 0, 0, 0, 0, 7]
]

solved_puzzle = [
    [6, 4, 3, 9, 2, 5, 1, 7, 8],
    [8, 1, 2, 6, 3, 7, 4, 9, 5],
    [9, 7, 5, 8, 1, 4, 3, 2, 6],
    [1, 8, 6, 3, 7, 9, 2, 5, 4],
    [2, 3, 7, 4, 5, 8, 9, 6, 1],
    [4, 5, 9, 2, 6, 1, 7, 8, 3],
    [5, 2, 1, 7, 8, 3, 6, 4, 9],
    [7, 9, 8, 1, 4, 6, 5, 3, 2],
    [3, 6, 4, 5, 9, 2, 8, 1, 7]
]

print(is_solved(puzzle))