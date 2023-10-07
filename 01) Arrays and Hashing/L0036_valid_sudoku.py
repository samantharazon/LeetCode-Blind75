
def validSudoku(board):
    
    cols = [set() for x in range(9)] #[set1, set2, set3, set4, set5, set6, set7, set8, set9]
    rows = [set() for x in range(9)] #[set1, set2, set3, set4, set5, set6, set7, set8, set9]
    squares = [[set() for x in range(3)] for y in range(3)] #  [ [set1, set2, set3],   
                                                            #    [set1, set2, set3],   
                                                            #    [set1, set2, set3] ]

    # NOTE: KEY/VALUE FOR SQUARES: kkey = (r/3, c/3)    value = hashset

    for r in range(9): # grid is 9 x 9
        for c in range(9):
            cell_value = board[r][c]
            if cell_value == ".": # skip empty space (represented by .)
                continue
            if (cell_value in rows[r] or    # if we find a duplicate (value exists in hashset)...
                cell_value in cols[c]  or
                cell_value in squares[r//3][c//3]): # integer division tells us current square we are in. 
                                                    # can be [0, #] [1, #] [2, #]
                return False

            # update hashset
            cols[c].add(cell_value)
            rows[r].add(cell_value)
            squares[r//3][c//3].add(cell_value)

    print("\nCOLS: ", cols)
    print("\nROWS: ", rows)
    print("\nSQUARES: ", squares)

    return True
                                                       # (r)
sudoku_board =  [["5","3",".",".","7",".",".",".","."] # i=0
                ,["6",".",".","1","9","5",".",".","."] # i=1
                ,[".","9","8",".",".",".",".","6","."] # i=2
                ,["8",".",".",".","6",".",".",".","3"] # i=3
                ,["4",".",".","8",".","3",".",".","1"] # i=4
                ,["7",".",".",".","2",".",".",".","6"] # i=5
                ,[".","6",".",".",".",".","2","8","."] # i=6
                ,[".",".",".","4","1","9",".",".","5"] # i=7
                ,[".",".",".",".","8",".",".","7","9"]]
result = validSudoku(sudoku_board)
print("\n1) ", result) # true

sudoku_board =  [["8","3",".",".","7",".",".",".","."]
                ,["6",".",".","1","9","5",".",".","."]
                ,[".","9","8",".",".",".",".","6","."]
                ,["8",".",".",".","6",".",".",".","3"]
                ,["4",".",".","8",".","3",".",".","1"]
                ,["7",".",".",".","2",".",".",".","6"]
                ,[".","6",".",".",".",".","2","8","."]
                ,[".",".",".","4","1","9",".",".","5"]
                ,[".",".",".",".","8",".",".","7","9"]]
result = validSudoku(sudoku_board)
print("\n2) ", result) # true

print("\n")