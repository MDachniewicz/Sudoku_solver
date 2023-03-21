from solver import Solution
import numpy as np

if __name__ == '__main__':
    board = [['3', '7', '.', '.', '5', '.', '2', '.', '.'],
             ['4', '.', '9', '7', '.', '6', '.', '1', '.'],
             ['.', '.', '1', '.', '.', '.', '.', '.', '.'],
             ['.', '.', '.', '1', '7', '.', '6', '4', '.'],
             ['.', '.', '.', '.', '.', '9', '.', '.', '.'],
             ['.', '9', '.', '.', '.', '.', '3', '.', '5'],
             ['.', '.', '.', '.', '2', '.', '.', '.', '.'],
             ['.', '5', '7', '8', '.', '.', '.', '.', '4'],
             ['.', '.', '.', '.', '.', '.', '.', '8', '.']]

    print(f'Board to solve: \n {np.array(board)}')
    sudoku = Solution(board)
    sudoku.solve_sudoku()



    #print(f'Solution: \n {np.array(board_expected)}')
    if sudoku.is_valid:
        print(f'Solved: \n {np.array(sudoku.board)}')
    else:
        print('Initial board is invalid')