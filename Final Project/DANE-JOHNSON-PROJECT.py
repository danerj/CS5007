#   Final Project
#   Author: <DANE> <JOHNSON> 
#   Save this file as DANE-JOHNSON-PROJECT.py

#   Note: You must have the files "sudoku1.csv", ... , "sudoku6.csv"
#   in the same directory as this .py file in order to run the program.


#   ------------------------
#   Part 0: Required Package
#   ------------------------

import csv

#   ---------------------------
#   Part 1: Sudoku Solver Class
#   ---------------------------

# Class Sudoku takes a sudoku puzzle from a csv file and
# includes the method solve() that writes in the solution.
class Sudoku:
    def __init__(self, filename):
        self.puzzle = []
        with open(filename) as csvfile:
            reader = csv.reader(csvfile, delimiter=';')
            for row in reader:
                self.puzzle.append(row)

        # Chosen format is to put 0's for the entries to be solved for and
        # convert the known string integer values to type 'int'.
        for i in range(9):
            for j in range(9):
                if self.puzzle[i][j] == '':
                    self.puzzle[i][j] = 0
                else:
                    self.puzzle[i][j] = int(self.puzzle[i][j])
                    
    def is_valid(self, row, column, value):
        for j in range(9):
            # Check if value matches any other element in the row.
            if self.puzzle[row][j] == value:
                return False
            # Check if value matches any other element in the column.
            if self.puzzle[j][column] == value:
                return False
            
        # Calculate the upper left corner for the square containing [row,column] 
        [p, q] = [row // 3 * 3, column // 3 * 3]
        # Check if value mathces any other element in the square
        for i in range(p, p + 3):
            for j in range(q, q + 3):
                if self.puzzle[i][j] == value and [i, j] != [row, column]:
                    return False
                
        return True
        
    def solve(self):
        for row in range(9):
            for column in range(9):
                # Find the next unspecified entry (0 is a placeholder)
                if self.puzzle[row][column] == 0:
                    # Find the first of 1,...,9 that can be legally written in.
                    for value in range(1, 10):
                        if self.is_valid(row, column, value):
                            # Assign the first legal value found and recurse
                            self.puzzle[row][column] = value
                            solved = self.solve()
                            if solved:
                                return solved
                            else:
                                # The legal value found did not work so try again.
                                self.puzzle[row][column] = 0
                    return False
        return True

#   ---------------
#   Part 2: Testing
#   ---------------

puzzle_files = [
    "sudoku1.csv",
    "sudoku2.csv",
    "sudoku3.csv",
    "sudoku4.csv",
    "sudoku5.csv",
    "sudoku6.csv"
    ]

for file in puzzle_files:
    s = Sudoku(file)
    print("Given sudoku puzzle:")
    for line in s.puzzle:
        print(line)
    s.solve()
    print("Solved sudoku puzzle:")
    for line in s.puzzle:
        print(line)
            


    

