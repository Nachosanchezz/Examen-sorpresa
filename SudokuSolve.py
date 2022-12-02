def sudoku(board):
    (x, y) = find_empty_cell(board)
    if (x, y) == (-1, -1):
        return True
    for i in {1,2,3,4,5,6,7,8,9}:
        if valid(x,y,i,board):
            board[x][y] = i
            if sudoku(board):
                return board
            board[x][y] = 0

