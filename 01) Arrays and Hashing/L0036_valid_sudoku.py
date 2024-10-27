
def validSudoku(board):
    # create an array containing 9 sets
    # [set1, set2, set3 ... set9]    
    cols = [set() for x in range(9)]
    rows = [set() for x in range(9)]

    # create an array containing 3 arrays + each array contains 3 sets
    # [ [set1..set3]  [set1..set3] [set1...set3] ]
    squares = [[set() for x in range(3)] for y in range(3)]

    for row in range(9):
        for col in range(9):
            cell_value = board[row][col]
            if cell_value == ".":
                continue   # end current iter in loop + go to the next iter.
            # if cell_value found, return False
            if (cell_value in rows[row] or
                cell_value in cols[col] or
                    cell_value in squares[row//3][col//3]):
                return False

            # update hashset
            cols[col].add(cell_value)
            rows[row].add(cell_value)
            squares[row//3][col//3].add(cell_value)

    print("\nCOLS: ", cols)
    print("\nROWS: ", rows)
    print("\nSQUARES: ", squares)

    return True

    # (r)
sudoku_board = [["5", "3", ".", ".", "7", ".", ".", ".", "."]  # i=0
                , ["6", ".", ".", "1", "9", "5", ".", ".", "."]  # i=1
                , [".", "9", "8", ".", ".", ".", ".", "6", "."]  # i=2
                , ["8", ".", ".", ".", "6", ".", ".", ".", "3"]  # i=3
                , ["4", ".", ".", "8", ".", "3", ".", ".", "1"]  # i=4
                , ["7", ".", ".", ".", "2", ".", ".", ".", "6"]  # i=5
                , [".", "6", ".", ".", ".", ".", "2", "8", "."]  # i=6
                , [".", ".", ".", "4", "1", "9", ".", ".", "5"]  # i=7
                , [".", ".", ".", ".", "8", ".", ".", "7", "9"]]
result = validSudoku(sudoku_board)
print("\n1) ", result)  # true

sudoku_board = [["8", "3", ".", ".", "7", ".", ".", ".", "."], ["6", ".", ".", "1", "9", "5", ".", ".", "."], [".", "9", "8", ".", ".", ".", ".", "6", "."], ["8", ".", ".", ".", "6", ".", ".", ".", "3"], ["4", ".", ".",
                                                                                                                                                                                                             "8", ".", "3", ".", ".", "1"], ["7", ".", ".", ".", "2", ".", ".", ".", "6"], [".", "6", ".", ".", ".", ".", "2", "8", "."], [".", ".", ".", "4", "1", "9", ".", ".", "5"], [".", ".", ".", ".", "8", ".", ".", "7", "9"]]
result = validSudoku(sudoku_board)
print("\n2) ", result)  # true

print("\n")
