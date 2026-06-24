
import numpy as np

grid =  [
            [0,0,8,0,0,0,0,1,6],
            [5,0,0,0,9,2,0,0,8],
            [0,0,0,1,0,0,0,0,0],
            [0,0,0,3,0,0,8,0,0],
            [0,2,0,0,0,0,0,7,0],
            [0,8,0,0,0,6,0,0,0],
            [0,0,0,0,0,3,0,0,0],
            [4,0,0,9,0,0,0,0,2],
            [0,6,0,0,0,0,7,0,0]
        ]

#traverse and check sudoku rules.
def valid_rules(row_index, column_index, number):
    global grid
    # to check row validation
    for i in range(0,9):
        if grid[row_index][i] == number:
            return False
    # to check column validation
    for i in range(0,9):
        if grid[i][column_index] == number:
            return False
    # to check square validation
    square_row =(row_index // 3) * 3
    square_column = (column_index // 3) * 3
    for i in range(0,3):
        for j in range(0,3):
            if grid[square_row + i][square_column + j] == number:
                return False
    return True

#to solve the sudoku
def solve():
    global grid
    #the start and end points of grid
    for row in range(0,9):
        for column in range(0,9):
            #only for spaces to be filled
            if grid[row][column] == 0:
                for number in range(1,10):
                    if valid_rules(row,column,number):
                        #if a number pass all the rules
                        grid[row][column] = number
                        if solve():
                            return True
                        #if not, back to zero
                        grid[row][column] = 0
                return False
    return True

if solve():
    print("your one unique solution is:")
    print(np.matrix(grid))
else:
    print("no solution exists")
