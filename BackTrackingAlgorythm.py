board = [
    [0 , 0 , 0 , 0 , 9 , 6 , 0 , 8 , 7],
    [0 , 7 , 0 , 5 , 0 , 4 , 6 , 1 , 0],
    [0 , 0 , 0 , 8 , 0 , 1 , 5 , 0 , 0],
    [0 , 9 , 2 , 0 , 0 , 0 , 3 , 4 , 1],
    [8 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 5],
    [5 , 1 , 3 , 0 , 0 , 0 , 7 , 9 , 0],
    [0 , 0 , 9 , 1 , 0 , 7 , 0 , 0 , 0],
    [0 , 8 , 4 , 2 , 0 , 9 , 0 , 3 , 0],
    [1 , 2 , 0 , 6 , 3 , 0 , 0 , 0 , 0]
]

def solve(board):
    find = find_empty(board)
    if not find:
        return True
    else:
        row, col = find
    for i in range(1,10):
        if valid(board,i,(row,col)):
            board[row][col] = i
            if solve(board):
                return True
            board[row][col] = 0
    return False

def valid(board,number,position):
    #Check Row
    for i in range(len(board[0])):
        if board[position[0]][i] == number and position[1] != i:
            return False

    #check Column
    for i in range(len(board)):
        if board[i][position[1]] == number and position[0] != i:
            return False

    #Check Box
    box_x = position[1]//3
    box_y = position[0]//3
    for i in range(box_y*3,box_y*3 + 3):
        for j in range(box_x*3,box_x*3 +3):
            if board[i][j] == number and (i,j) != position:
                return False
    return True
    # for i in range(box_y*3,box_x*3):

def print_board(board):
    for i in range(len(board)):
        if i %3 == 0:
            print("=======================")
        for j in range(len(board[0])):
            if j % 3 == 0 and j !=0:
                print("|| ",end="")
            if j == 8:
                print(board[i][j])
            else:
                print(f"{board[i][j]} ", end="")
    print("=======================")
def find_empty(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                return (i,j) #row,column
    return None
print_board(board)
solve(board)
print_board(board)