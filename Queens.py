def nQueens(n):
    result = []
    SolveNQueens(n,0,[],result)
    return result
def isValid(placement):
    rowId = len(placement)-1
    for i in range(rowId):
        diff = abs(placement[i] - placement[rowId])
        if diff == 0 or diff == rowId-i:
            return False
    return True
def SolveNQueens(dimension,row,placement,result):
    if row == dimension:
        print(type(placement))
        print(placement)
        # result.extend(placement)
        result.append(placement)
    else:
        for i in range(dimension):
            placement.append(i)
            if isValid(placement):
                SolveNQueens(dimension,row+1,placement,result)
            placement.pop()
board = nQueens(4)
# for i in range(len(nQueens(4))):
#     print(i)
# for i in range(len(board)):
#     if i % 3 == 0:
#         print(board[i])
#     else:
#         print(board[i],end="")
print(board)
# print(f"{board[:4]}\n{board[4:8]}\n{board[8:12]}\n{board[12:]}")