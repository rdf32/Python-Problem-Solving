import numpy as np
from Sudoku import engine

if __name__ == "__main__":

    # assigning values to the grid
    board = np.array([
        [0, 0, 0, 0, 0, 0, 2, 0, 0],
        [0, 8, 0, 0, 0, 7, 0, 9, 0],
        [6, 0, 2, 0, 0, 0, 5, 0, 0],
        [0, 7, 0, 0, 6, 0, 0, 0, 0],
        [0, 0, 0, 9, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 2, 0, 0, 4, 0],
        [0, 0, 5, 0, 0, 0, 6, 0, 3],
        [0, 9, 0, 4, 0, 0, 0, 7, 0],
        [0, 0, 6, 0, 0, 0, 0, 0, 0]
    ])
    board_solution = np.array([
        [9, 5, 7, 6, 1, 3, 2, 8, 4],
        [4, 8, 3, 2, 5, 7, 1, 9, 6],
        [6, 1, 2, 8, 4, 9, 5, 3, 7],
        [1, 7, 8, 3, 6, 4, 9, 5, 2],
        [5, 2, 4, 9, 7, 1, 3, 6, 8],
        [3, 6, 9, 5, 2, 8, 7, 4, 1],
        [8, 4, 5, 7, 9, 2, 6, 1, 3],
        [2, 9, 1, 4, 3, 6, 8, 7, 5],
        [7, 3, 6, 1, 8, 5, 4, 2, 9]
    ])
    # create Solver instance
    solve_board = engine.Solver(board)
    # get solution
    solution = solve_board.solve(board)


