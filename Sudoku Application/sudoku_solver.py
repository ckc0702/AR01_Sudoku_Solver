"""
Options of algorithm: naive, backtracking, cross-hatching

Naive -
The naive approach is to generate all possible configurations of numbers from 1 to 9 to fill the empty cells.
Try every configuration one by one until the correct configuration is found, i.e. for every unassigned position fill the
position with a number from 1 to 9. After filling all the unassigned positions check if the matrix is safe or not. If
safe print else recurs for other cases.

Backtracking -
Like all other Backtracking problems, Sudoku can be solved by assigning numbers one by one to empty cells.
Before assigning a number, check whether it is safe to assign.

Check that the same number is not present in the current row, current column and current 3X3 subgrid.
After checking for safety, assign the number, and recursively check whether this assignment leads to a solution or not.
If the assignment doesn’t lead to a solution, then try the next number for the current empty cell. And if none of the
number (1 to 9) leads to a solution, return false and print no solution exists.
"""


def find_empty_cell(bo):
    for i in range(9):
        for j in range(9):
            if bo[i][j] == 0:
                return i, j  # row, col
    return None


def number_isvalid(bo, num, pos):
    # Check Row
    for i in range(9):
        if num == bo[pos[0]][i]:
            return False

    # Check Column
    for i in range(9):
        if num == bo[i][pos[1]]:
            return False

    # Check Box (3x3)
    box_x = pos[0] // 3
    box_y = pos[1] // 3

    for i in range(box_x*3, box_x*3+3):
        for j in range(box_y*3, box_y*3+3):
            if num == bo[i][j]:
                return False

    return True


def naive_algorithm(bo, row, col):
    """
    1. Loop through each cell to find unfilled cell
    2. Check constraint on current row, col, and box
    3. If have valid number place in empty cell, and do recursion
    4. Else re-assign value to zero
    4. If reach 9th col, move to next row
    """
    #print(bo)
    if row == 9 - 1 and col == 9:
        return True

    if col == 9:
        row += 1
        col = 0

    if bo[row][col] > 0:
        return naive_algorithm(bo, row, col + 1)
    for num in range(1, 9 + 1, 1):

        if number_isvalid(bo, num, [row, col]):

            bo[row][col] = num

            if naive_algorithm(bo, row, col + 1):
                return True

        bo[row][col] = 0
    return False


def backtracking_algorithm(bo):
    """
    1. Find unfilled cell
    2. Check constraint on current row, col, and box
    3. If have valid number place in empty cell, and do recursion
    4. Else backtrack
    5. Do process until all cell is filled
    """
    #print(bo)
    empty_cell = find_empty_cell(bo)
    if not empty_cell:
        return True
    else:
        for i in range(1, 10):
            if number_isvalid(bo, i, empty_cell):
                bo[empty_cell[0]][empty_cell[1]] = i

                if backtracking_algorithm(bo):
                    return True

                bo[empty_cell[0]][empty_cell[1]] = 0

        return False
