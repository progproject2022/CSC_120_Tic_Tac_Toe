board = [["-", "-", "-"],
         ["-", "-", "-"],
         ["-", "-", "-"]]

player = "X"

#Functions
def showBoard():
    print("Drawing Board...")
    for r in range(3):
        print(board[r])

#Error Handling Functions
def validate_row(x):
    while not(x >= 0 and x <= 2):
        print('Invalid Row')
        x = int(input("Enter a new row number (0-2): "))
        if x >= 0 and x <= 2:
            return x
    if x >= 0 and x <= 2:
        return x

def validate_col(y):
    while not(y >= 0 and y <= 2):
        print('invalid Column')
        y = int(input("Enter a new column number (0-2): "))
        if y >= 0 and y <= 2:
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

def move(r, c):
    board[r][c] = player

def switchPlayer():
    if (player == "X"):
        return "O"
    elif (player == "O"):
        return "X"

#Events
print("Let's Play!")
gameOver = False

#Game Loop
while (not gameOver):
    showBoard()
    print("Player " + player + ", make a move")
    row = int(input("Enter a row number (0-2): "))
    row = validate_row(row)
    col = int(input("Enter a column number (0-2): "))
    col = validate_col(col)
    coor = overlap(row, col)
    row = coor[0]
    col = coor[1]
    gameOver = move(row, col)
    if (not gameOver):
        player = switchPlayer()

