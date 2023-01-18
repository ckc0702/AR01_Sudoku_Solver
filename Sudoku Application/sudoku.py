from sudoku_solver import naive_algorithm
from sudoku_solver import backtracking_algorithm


def draw_board(bo):
    for i in range(len(bo)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - - ")

        for j in range(len(bo[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="") #end prevent /n new line

            if j == 8: #if end of row print /n
                print(bo[i][j])
            else: #print number on board
                print(str(bo[i][j]) + " ", end="")


if __name__ == "__main__":

    # creating a 2D array for the grid (9x9)
    board = [[0 for x in range(9)] for y in range(9)]

    # Sample Questions
    board1 = [
        [7, 8, 0, 4, 0, 0, 1, 2, 0],
        [6, 0, 0, 0, 7, 5, 0, 0, 9],
        [0, 0, 0, 6, 0, 1, 0, 7, 8],
        [0, 0, 7, 0, 4, 0, 2, 6, 0],
        [0, 0, 1, 0, 5, 0, 9, 3, 0],
        [9, 0, 4, 0, 6, 0, 0, 0, 5],
        [0, 7, 0, 3, 0, 0, 0, 1, 2],
        [1, 2, 0, 0, 0, 7, 4, 0, 0],
        [0, 4, 9, 2, 0, 6, 0, 0, 7]
    ]

    board2 = [
        [0, 0, 0, 0, 0, 0, 1, 8, 0],
        [6, 0, 0, 7, 0, 2, 0, 3, 0],
        [7, 0, 4, 0, 0, 3, 0, 0, 5],
        [0, 0, 5, 6, 0, 0, 0, 4, 3],
        [0, 9, 0, 1, 0, 0, 2, 0, 8],
        [0, 0, 0, 0, 8, 0, 9, 0, 0],
        [0, 0, 1, 5, 0, 0, 0, 0, 2],
        [0, 0, 3, 9, 6, 0, 0, 7, 0],
        [5, 6, 7, 0, 0, 4, 0, 0, 0]
    ]

    board3 = [
        [3, 0, 6, 5, 0, 8, 4, 0, 0],
        [5, 2, 0, 0, 0, 0, 0, 0, 0],
        [0, 8, 7, 0, 0, 0, 0, 3, 1],
        [0, 0, 3, 0, 1, 0, 0, 8, 0],
        [9, 0, 0, 8, 6, 3, 0, 0, 5],
        [0, 5, 0, 0, 9, 0, 6, 0, 0],
        [1, 3, 0, 0, 0, 0, 2, 5, 0],
        [0, 0, 0, 0, 0, 0, 0, 7, 4],
        [0, 0, 5, 2, 0, 6, 3, 0, 0]
    ]

    draw_board(board3)
    # naive_algorithm(board3, 0, 0)
    backtracking_algorithm(board3)
    print("-------------Answer------------------")
    draw_board(board3)


