import numpy as np


def draw_board():
    # creates a blank board as a list
    board_list = (['_', '_', '_'],
                  ['_', '_', '_'],
                  ['_', '_', '_'])
    # converts our list into a array with numpy
    board = np.array(board_list)
    # makes sure our array is stored in string values
    str(board)
    print(board)

    def board_input():
        print('Player 1, make your move')
        p1_move_row = int(input('Enter row number (0-2): '))
        p1_move_col = int(input('Enter col number (0-3): '))
        board[p1_move_col, p1_move_row] = 'X'
        print(board)
    board_input()


draw_board()

