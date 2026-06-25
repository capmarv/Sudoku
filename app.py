from flask import Flask, render_template, request

app = Flask(__name__)

#traverse and check sudoku rules.
def valid_rules(grid,row_index, column_index, number):

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
def solve(grid):

    #the start and end points of grid
    for row in range(0,9):
        for column in range(0,9):
            #only for spaces to be filled
            if grid[row][column] == 0:
                for number in range(1,10):
                    if valid_rules(grid, row,column,number):
                        #if a number pass all the rules
                        grid[row][column] = number
                        if solve(grid):
                            return True
                        #if not, back to zero
                        grid[row][column] = 0
                return False
    return True

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/solve", methods=["POST"])
def solve_board():
    grid = []

    for row in range(9):
        current_row = []

        for col in range(9):
            value = request.form.get(f"cell_{row}_{col}")

            if value == "":
                value = 0
            else:
                value = int(value)

            current_row.append(value)
            
        grid.append(current_row)

    if solve(grid):
        return str(grid)
    else:
        return "No solution exists"

if __name__ == "__main__":
    app.run(debug=True)