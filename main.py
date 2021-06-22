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
    while not is_solved(board):
        row = 0
        column = 0
        queue = []
        if 0 in board[row]:
            column = board[row].index(0)
        else:
            row += 1
        possible = generate_valid_set(row, column, board)
        iteration = iter(sorted(possible))
        temp = next(iteration)
        queue.append(iteration)
        if temp == None:
            # Figure out how to move to the next iteration
        board[row][column] = temp



# Generates valid set to use for continued solving
def generate_valid_set(row, column, board):
    row_set = set(board[row])
    col_set = set()

    # Generates column set
    for col in range(len(board[row])):
        col_set.add(board[row][col])
    col_set.discard(0)

    # Generates box set
    box_lookup = findbox(row, column)
    box_set = set()
    for i in range(int(box_lookup[0]) - 3, int(box_lookup[0])):
        for j in range(int(box_lookup[1]) - 3, int(box_lookup[1])):
            box_set.add(board[i][j])
    box_set.discard(0)

    # Unifies all sets to generate a valid set
    val_set = {1, 2, 3, 4, 5, 6, 7, 8, 9} - (row_set | col_set | box_set)
    return val_set


# Using the box_table, finds the appropriate box of the column and row specified
def findbox(row, column):
    ret = ''
    if row in range(0, 3):
        ret += '3'
    elif row in range(3, 6):
        ret += '6'
    else:
        ret += '9'

    if column in range(0, 3):
        ret += '3'
    elif column in range(3, 6):
        ret += '6'
    else:
        ret += '9'
    return ret


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
