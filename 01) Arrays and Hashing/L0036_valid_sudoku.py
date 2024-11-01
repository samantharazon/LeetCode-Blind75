from collections import defaultdict

def validSudoku(board):
    cols = defaultdict(set)     # [set1, set2, set3 ... set9]  
    rows = defaultdict(set)     # [set1, set2, set3 ... set9]  
    squares = defaultdict(set)  # [ [set1..set3]  [set1..set3] [set1...set3] ]

    for r in range(9):
        for c in range(9):
            cell_value = board[r][c]

            if cell_value == ".":
                continue

            if (cell_value in cols[c] or
                cell_value in rows[r] or
                cell_value in squares[(r//3, c//3)]):
                return False
            
            cols[c].add(cell_value)
            rows[r].add(cell_value)
            squares[(r//3, c//3)].add(cell_value)
    return True

print("\nSudoku #1)")
sudoku_board = [  ["5", "3", ".", ".", "7", ".", ".", ".", "."]  # i=0
                , ["6", ".", ".", "1", "9", "5", ".", ".", "."]  # i=1
                , [".", "9", "8", ".", ".", ".", ".", "6", "."]  # i=2
                , ["8", ".", ".", ".", "6", ".", ".", ".", "3"]  # i=3
                , ["4", ".", ".", "8", ".", "3", ".", ".", "1"]  # i=4
                , ["7", ".", ".", ".", "2", ".", ".", ".", "6"]  # i=5
                , [".", "6", ".", ".", ".", ".", "2", "8", "."]  # i=6
                , [".", ".", ".", "4", "1", "9", ".", ".", "5"]  # i=7
                , [".", ".", ".", ".", "8", ".", ".", "7", "9"]]
result = validSudoku(sudoku_board)
print("Valid:", result)  # true

print("\nSudoku #2)")
sudoku_board = [["8", "3", ".", ".", "7", ".", ".", ".", "."], 
                ["6", ".", ".", "1", "9", "5", ".", ".", "."], 
                [".", "9", "8", ".", ".", ".", ".", "6", "."], 
                ["8", ".", ".", ".", "6", ".", ".", ".", "3"], 
                ["4", ".", ".", "8", ".", "3", ".", ".", "1"], 
                ["7", ".", ".", ".", "2", ".", ".", ".", "6"], 
                [".", "6", ".", ".", ".", ".", "2", "8", "."], 
                [".", ".", ".", "4", "1", "9", ".", ".", "5"], 
                [".", ".", ".", ".", "8", ".", ".", "7", "9"]]
result = validSudoku(sudoku_board)
print("Valid:", result)  # true

print("\n")