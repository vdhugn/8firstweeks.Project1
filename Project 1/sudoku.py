board = [[int(x) for x in input().split()] for _ in range(9)]

def isValid(board, row, col, num):
    for i in range(9):
        if board[row][i] == num or board[i][col] == num:
            return False

    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(3):
        for j in range(3):
            if board[i + start_row][j + start_col] == num:
                return False
    return True

def sudoku(board):
    count = 0
    def backtracking(row, col):
        nonlocal count
        if row == 9:
            count += 1
            return       
        next_row, next_col = (row, col + 1) if col < 8 else (row + 1, 0)
        if board[row][col] == 0:
            for num in range(1, 10):
                if isValid(board, row, col, num):
                    board[row][col] = num
                    backtracking(next_row, next_col)
                    board[row][col] = 0
        else:
            backtracking(next_row, next_col)
    backtracking(0, 0)
    return count

print(sudoku(board))