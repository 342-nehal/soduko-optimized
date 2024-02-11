def solveSudoku():
    """
    Do not return anything, modify board in-place instead.
    """
    global counter
    
    def isSafe(i,j,k):
        for l in range(9):
            if board[l][j]==k or board[i][l]==k:
                return False
        startrow=(i//3)*3
        startcol=(j//3)*3
        for a in range(startrow,startrow+3):
            for b in range(startcol,startcol+3):
                if board[a][b]==k:
                    return False
        return True
    def f():
        global counter
        for i in range(9):
            for j in range(9):
                if board[i][j]==0:
                    for k in range(1,10):
                        if isSafe(i,j,k):
                            board[i][j]=k
                            counter+=1
                            r=f()
                            if r:
                                return True
                            board[i][j]=0
                    return False
        return True
    # check if the number is the only possible number in a particular row, column or block
    n=2
    for i in range(n):
        for i in range(9):
            for j in range(9):
                if board[i][j]==0:
                    count=0
                    for k in range(1,10):
                        if isSafe(i,j,k):
                            ele=k
                            count+=1
                            if count>=2:
                                break
                    if count==1:
                        board[i][j]=ele
    
    f()
    return board
counter=1
board=[[3 ,0, 6, 5, 0, 8, 4, 0, 0],
    [5, 2, 0, 0, 0, 0, 0, 0, 0],
    [0, 8, 7, 0, 0, 0, 0, 3, 1],
    [0, 0, 3, 0, 1, 0, 0, 8, 0],
    [9, 0, 0, 8, 6, 3, 0, 0, 5],
    [0, 5, 0, 0, 9, 0, 6, 0, 0,],
    [1, 3, 0, 0, 0, 0, 2, 5, 0],
    [0, 0, 0, 0, 0, 0, 0, 7, 4],
    [0, 0, 5, 2, 0, 6, 3, 0, 0,]]

print(solveSudoku())
print(counter)

