import unittest

class Board(object):
    def __init__(self):
        self.board = [['-', '-', '-'], ['-', '-', '-'], ['-', '-', '-']]

    pass

    def mark_square(self, column, row, player):
        if player == 'x':
            mark = 'x'
        else:
            mark = 'o'
        if self.board[int(row)][int(column)] == '-':
            self.board[int(row)][int(column)] = mark
            return True
        else:
            print("invalid location")
            return False

    pass


    def has_winner(self):
        return (self.board[0][0] == self.board[0][1] == self.board[0][2] != '-') or (self.board[1][0] == self.board[1][1] == self.board[1][2] != '-') or (self.board[2][0] == self.board[2][1] == self.board[2][2] != '-') or (self.board[0][0] == self.board[1][0] == self.board[2][0] != '-') or (self.board[0][1] == self.board[1][1] == self.board[2][1] != '-') or (self.board[0][2] == self.board[1][2] == self.board[2][2] != '-') or (self.board[0][0] == self.board[1][1] == self.board[2][2] != '-') or (self.board[2][0] == self.board[1][1] == self.board[0][2] != '-')

    def play_game(self):
        while not self.has_winner():
            val=input("Enter move in form: Column, Row, Symbol\n")
            val = val.split(', ')
            if self.validate_input(val):
                print("success")
                self.mark_square(val[0], val[1], val[2])
                self.printBoard()
            else:
                print("try again")


        return 0

    def validate_input(self, vals):
        if len(vals) == 3:
            for i in range(len(vals)):
                if len(vals[i]) != 1:
                    return False
                else:
                    continue
            return True
        else:
            return False

    def printBoard(self):
        print(self.board[0])
        print(self.board[1])
        print(self.board[2])

class TestBoard(unittest.TestCase):

    def __init__(self):
        self.board = Board()

    def test_initialization(self):
        self.assertEqual(self.board.board[0], ['-', '-', '-'])

if __name__ == '__main__':
    board = Board()
    unittest.main()
    winner = board.play_game()
    print("{} has won!".format(winner))
