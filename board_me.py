import numpy as np

# creates a blank board as a list

board_list = (['_', '_', '_'],
              ['_', '_', '_'],
              ['_', '_', '_'])
# converts our list into a array with numpy
board = np.array(board_list)
# makes sure our array is stored in string values
str(board)


def write_board_p1(x, y):
    board[x, y] = 'X'
    print('Drawing board....')
    print(board)


def write_board_p2(x, y):
    board[x, y] = 'O'
    print('Drawing board....')
    print(board)


def validate_row(x):
    while x > 2 or x < 0:
        print('invalid input')
        x = int(input('Enter row number (0-2): '))
        if 0 <= x <= 2:
            return x
    if 0 <= x <= 2:
        return x
    while 'X' or 'O' in board[x]:
        print('Spot is taken try again')
        x = int(input('Enter a valid row number (0-2): '))
        if 'X' or 'O' not in board[x]:
            return x


def validate_column(y):
    while y > 2 or y < 0:
        print('invalid input')
        y = int(input('Enter column number (0-2): '))
        if 0 <= y <= 2:
            return y
    while 'X' in board[y] or 'O' in board[y]:
        print('Spot is taken try again')
        y = int(input('Enter a valid column number (0-2): '))
        if 'X' not in board[y] and 'O' not in board[y]:
            return y
    if 0 <= y <= 2:
        return y


def board_input():
    print('Player 1, make your move')
    x1 = int(input('Enter row number (0-2): '))
    x1 = validate_row(x1)
    y1 = int(input('Enter col number (0-2): '))
    y1 = validate_column(y1)
    write_board_p1(x1, y1)

    print('Player 2, make your move')
    x2 = int(input('Enter row number (0-2): '))
    validate_row(x2)
    y2 = int(input('Enter col number (0-2): '))
    validate_column(y2)
    write_board_p2(x2, y2)
    check_win()


def check_win():
    if 'X' in board[0, 0] and board[0, 1] and board[0, 2]:
        print('Player one wins!')


print('Drawing board....')
print(board)
board_input()









