import math
import time
from player import HumanPlayer, RandomComputerPlayer, SmartComputorPlayer 

class TicTacToe():
    # func to initialize the board n a winner which is set to None
    def __init__(self):
        self.board = self.make_board()
        self.current_winner = None

    @staticmethod
    # a func to return a board with 9 spaces
    def make_board():
        return [' ' for _ in range(9)]
    

    def print_board(self):
        # !for visual purposes only
        # going through 3 rows and just printing those 3 rows
        for row in [self.board[i * 3: (i + 1) * 3 ] for i in range(3)]:
            print('| ' + ' | '.join(row) + ' |')


    @staticmethod
    # assigns the value 0 - 8 to every single space on the board
    # 0 | 1 | 2 
    # 3 | 4 | 5 
    # 6 | 7 | 8 
    def print_board_nums():
        number_board = [[str(i) for i in range (j * 3, (j + 1)* 3)] for j in range(3)]
        for row in number_board:
            print(' | '  + ' | '.join(row) + ' |')

    # this func is taking a square(represents which space the user wants to go, num 0-8) 
    # and a letter X or O
    def make_move(self, square, letter):
        # check to see if the space is empty
        if self.board[square] == ' ':
            # if it is assign a letter to that square
            self.board[square] = letter
            # check if its a winner
            if self.winner(square, letter):
                # if it is curr winner assign to curr player
                self.current_winner = letter
            return True
        return False

    # basically a func to check if a move made me a W or no
    def winner(self, square, letter):
        # check the row
        row_ind = math.floor(square / 3)
        row = self.board[row_ind*3:(row_ind+1)*3]
        # print('row', row)
        # so if all letters are the same its a W
        if all([s == letter for s in row]):
            return True
        
        # now check all the letter in the column
        col_ind = square % 3
        column = [self.board[col_ind+i*3] for i in range(3)]
        # print('col', column)
        if all([s == letter for s in column]):
            return True
        
        # to check the diagonal 
        # 1. check if square is even
        # 2. if they are then i gonna take diagonal squares such as [0, 4, 8] or [2, 4, 6]
        if square % 2 == 0:
            diagonal1 = [self.board[i] for i in [0, 4, 8]]
            # print('diag1', diagonal1)
            if all([s == letter for s in diagonal1]):
                return True
            diagonal2 = [self.board[i] for i in [2, 4, 6]]
            # print('diag2', diagonal2)
            if all([s == letter for s in diagonal2]):
                return True
        return False
