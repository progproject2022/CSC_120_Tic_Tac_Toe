board = [["-", "-", "-"],
         ["-", "-", "-"],
         ["-", "-", "-"]]

player = "X"


# Functions
def show_board():
    print("Drawing Board...")
    for r in range(3):
        print(board[r])


# Error Handling Functions
def validate_row(x):
    while not (x >= 0 and x <= 2):
        print('Invalid Row')
        x = int(input("Enter a new row number (0-2): "))
        if 0 <= x <= 2:
            return x
    if 0 <= x <= 2:
        return x


def validate_col(y):
    while not (y >= 0 and y <= 2):
        print('invalid Column')
        y = int(input("Enter a new column number (0-2): "))
        if 0 <= y <= 2:
            return y
    if 0 <= y <= 2:
        return y


def overlap(r, c):
    while board[r][c] == "X" or board[r][c] == "Y":
        print("This spot is taken")
        r = int(input('Enter new row number (0-2): '))
        c = int(input('Enter new column number (0-2): '))
        if not(board[r][c] == "X" or board[r][c] == "Y"):
            return [r, c]
    if not(board[r][c] == "X" or board[r][c] == "Y"):
        return [r, c]


# Win-Checking Functions
def h_win():
    count = 0
    for r in range(3):
        for c in range(3):
            if board[r][c] == player:
                count += 1
        if count == 3:
            return True
        count = 0
    return False


def v_win():
    count = 0
    for c in range(3):
        for r in range(3):
            if board[r][c] == player:
                count += 1
        if count == 3:
            return True
        count = 0
    return False


def d_win():
    count = 0
    for r in range(3):
        for c in range(3):
            if r == c and board[r][c] == player:
                count += 1
    if count == 3:
        return True
    return False


def rd_win():
    count = 0
    for r in range(0, len(board) - 1):
        for c in range(len(board) - 1, -1, -1):
            if board[r][c] == player and board[r + 1][c - 1] == player:
                count += 1
    if count == 2:
        return True
    return False


def did_current_player_win():
    if h_win() or v_win() or d_win() or rd_win():
        return True
    else:
        return False


def tie():
    for r in range(3):
        for c in range(3):
            if board[r][c] == "-":
                return False
    return True


def move(r, c):
    board[r][c] = player
    if did_current_player_win() or tie():
        return True
    return False


def switch_player():
    if player == "X":
        return "O"
    elif player == "O":
        return "X"


# Events
print("Let's Play!")
gameOver = False

# Game Loop
while not gameOver:
    show_board()
    print("Player " + player + ", make a move")
    row = int(input("Enter a row number (0-2): "))
    row = validate_row(row)
    col = int(input("Enter a column number (0-2): "))
    col = validate_col(col)
    coor = overlap(row, col)
    row = coor[0]
    col = coor[1]
    gameOver = move(row, col)
    if not gameOver:
        player = switch_player()

#Game Results
show_board()
if tie():
    print("This game has ended in a tie!")
else:
    print("Player " + player + " has won!")

