# Question: https://www.codewars.com/kata/5296bc77afba8baa690002d7/train/python

# Solution:                   
M = 9                        
def sudoku(board):
    def isValid(digit, i, j):
        # Checking validity for columns
        for y in range(M):
            if board[i][y] == digit:   return False
        # Checking validity for rows
        for x in range(M):
            if board[x][j] == digit:   return False
        # Checking validity for 3x3 Square
        square_x, square_y = i//3, j//3
        for x in range(square_x*3, square_x*3+3):
            for y in range(square_y*3, square_y*3+3):
                if board[x][y] == digit:   return False
        return True
    def search(i, j):
        if i == M:
            return True
        elif j == M:
            return search(i+1, 0)
        if board[i][j] == 0:
            for digit in range(1, M+1):
                if isValid(digit, i, j):
                    board[i][j] = digit
                    if search(i, j+1): 
                        return True
                    board[i][j] = 0
            return False
        else:
            return search(i, j+1)
    search(0,0)
    return board
