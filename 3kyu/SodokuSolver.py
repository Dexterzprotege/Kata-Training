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

# Sample Tests:
'''
test.describe('Sudoku')

puzzle = [[5,3,0,0,7,0,0,0,0],
          [6,0,0,1,9,5,0,0,0],
          [0,9,8,0,0,0,0,6,0],
          [8,0,0,0,6,0,0,0,3],
          [4,0,0,8,0,3,0,0,1],
          [7,0,0,0,2,0,0,0,6],
          [0,6,0,0,0,0,2,8,0],
          [0,0,0,4,1,9,0,0,5],
          [0,0,0,0,8,0,0,7,9]]

solution = [[5,3,4,6,7,8,9,1,2],
            [6,7,2,1,9,5,3,4,8],
            [1,9,8,3,4,2,5,6,7],
            [8,5,9,7,6,1,4,2,3],
            [4,2,6,8,5,3,7,9,1],
            [7,1,3,9,2,4,8,5,6],
            [9,6,1,5,3,7,2,8,4],
            [2,8,7,4,1,9,6,3,5],
            [3,4,5,2,8,6,1,7,9]]

test.it('Puzzle 1')
test.assert_equals(sudoku(puzzle), solution, "Incorrect solution for the following puzzle: " + str(puzzle));
'''
