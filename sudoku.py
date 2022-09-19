board = []
board_file = open('boardFile.txt')

## Reading the file and creating the board line  by line
for line in board_file:
    board.append(list(map(int, line.strip())))

## Formatting the board in an user readable way
def board_layout(board):
    for i in range(0,9):
        if(i%3 == 0 and i != 0):
            print("- " * 13)
        for x in range(0,9):
            if(x%3 == 0 and x != 0):
                print(" | ", end="")

            if x != 8:
                print(board[i][x], end=" ")
            else:
                print(board[i][x])

## Checking if the possible number to be entered meets the requirements of the game 
def valid(row, column, number):
    for i in range(0,9):
        if(board[row][i] == number):
            return False

    for i in range(0,9):
        if(board[i][column] == number):
            return False

    rowS = (row // 3) * 3
    columnS = (column // 3) * 3
    for i in range(0,3):
        for x in range(0,3):
            if(board[rowS+i][columnS+x] == number):
                return False
    return True

## Finds the empty tile on the board and solves the board
def solution():
    for row in range(0,9):
        for column in range(0,9):
            if(board[row][column] == 0):
                for number in range (1,10):
                    if(valid(row, column, number)):
                        board[row][column] = number
                        solution()
                        board[row][column] = 0
                return
    board_layout(board)

board_layout(board)
print("\n")
solution()
