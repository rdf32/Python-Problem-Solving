# ideas for the future
# maybe make it a Play class and let them play, then just have the solver method
# implement pyauto gui for graphical interface
## THINGS TO DO ##
# comment code
# add printing method to clean it up or create a variable that holds solution
SQDict = {}
for i in range(9):
    for j in range(9):
        SQDict[(i, j)] = (i // 3, j // 3)

class Solver():
    def __init__(self, board):
        self.board = board


    def find_empty(self, loc):

        for i in range(len(self.board)):
            for j in range(len(self.board)):
                if self.board[i][j] == 0:
                    loc[0] = i
                    loc[1] = j
                    return True
        return False

    def get_sq(self, row, col):
        sq = SQDict[(row, col)]

        return sq

    def in_row(self, row, num):

        for i in range(9):
            if self.board[row][i] == num:
                return True
        return False


    def in_col(self, col, num):

        for i in range(9):
            if self.board[i][col] == num:
                return True
        return False

    def in_square(self, row, col, num):

        sq = self.get_sq(row, col)

        for i in range(sq[0] * 3, sq[0] * 3 + 3):
            for j in range(sq[1] * 3, sq[1] * 3 + 3):
                if self.board[i][j] == num and (i, j) != (row, col):
                    return True
        return False

    def valid_location(self, row, col, num):
        return (not self.in_row(row, num)) and \
               (not self.in_col(col, num)) and \
               (not self.in_square(row, col, num))

    def solve(self, board):

        loc = [0, 0]
        if not self.find_empty(loc):
            return True, print(board)


        row = loc[0]
        col = loc[1]

        for num in range(1, 10):

            if self.valid_location(row, col, num):

                board[row][col] = num

                if self.solve(board):
                    return True

                self.board[row][col] = 0

        return False


