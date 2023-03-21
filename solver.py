class Solution:
    def __init__(self, board):
        self.is_solved = False
        self.is_valid = True
        self.board = board
        self.row_contains = [[False for i in range(9)] for j in range (9)]
        self.column_contains = [[False for i in range(9)] for j in range (9)]
        self.cell_contains = [[False for i in range(9)] for j in range (9)]

    def _get_cell(self, row, col):
        return (row // 3) * 3 + col // 3

    def _get_next_row(self, row, col):
        return row + (col + 1) // 9

    def _get_next_col(self, col):
        return (col + 1) % 9

    def _next_empty_position(self, board, row, col):
        while row != 9:
            if board[row][col] == '.':
                return row, col
            row = self._get_next_row(row, col)
            col = self._get_next_col(col)

        return 9, 0

    def solve_sudoku(self):
        for row in range(9):
            for col in range(9):
                cell = self._get_cell(row, col)
                contains = [a or b or c for a, b, c in
                            zip(self.row_contains[row], self.column_contains[col], self.cell_contains[cell])]
                digit = self.board[row][col]
                if digit != '.':
                    digit = int(digit)-1
                    if contains[digit]:
                        self.is_valid = False
                        return
                    self.row_contains[row][digit] = True
                    self.column_contains[col][digit] = True
                    cell = self._get_cell(row, col)
                    self.cell_contains[cell][digit] = True

        self._solve(0, 0)

        if '.' not in self.board and self.is_valid:
            self.is_solved = True

    def _solve(self, row_start, col_start):
        row, col = self._next_empty_position(self.board, row_start, col_start)
        if row == 9:
            return True
        cell = self._get_cell(row, col)
        contains = [a or b or c for a, b, c in zip(self.row_contains[row], self.column_contains[col], self.cell_contains[cell])]
        #contains = self.row_contains[row] or self.column_contains[col] or self.cell_contains[cell]
        if all(contains):
            return False

        for digit in range(9):
            if not contains[digit]:
                self.board[row][col] = str(digit+1)
                self.row_contains[row][digit] = True
                self.column_contains[col][digit] = True
                self.cell_contains[cell][digit] = True
                if self._solve(row, col):
                    return True

                self.row_contains[row][digit] = False
                self.column_contains[col][digit] = False
                self.cell_contains[cell][digit] = False
        self.board[row][col] = '.'
        return False

    def __str__(self):
        return self.board
