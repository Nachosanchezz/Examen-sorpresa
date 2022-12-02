def sudoku(board):
    (x, y) = find_empty_cell(board)
    if (x, y) == (-1, -1):
        return True
        
