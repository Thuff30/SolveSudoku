This is a simple Tkinter GUI based Python application that can solve Sudoku puzzles. It has been tested successfully using a variety of difficulty puzzles from varied sources.
The puzzle is solved using 3 functions that implement for loops, recursion, and backtracking. Recursion, if used correctly, helps to minimize excess code by reusing the
existing lines. Backtracking helps to reduce excess code by resetting answers that do not work without the need for extra functions and duplicate lists.

The functions used are submit_input, reviewpossibles, clear_puzzle, solvepuzzle, and show_solution. 
submit_input converts the user's input into a list of integers for each row then combines those lists into one master list.
reviewpossibles examines a square in the Sudoku puzzle that is passed into it. It cycles through each possible number (1-9) and checks them against the other squares in 
the same row and column to determine if they are a viable answer. 
clear_puzzle allows the user to clear the contents of the puzzle in the case of an error or simply to try another puzzle.
solvepuzzle if fairly self explanatory in that it cycles through every position in the Sudoku puzzle and passes them into the reviewpossibles puzzle. This function is where the recursion and backtracking occur.
show_solution displays the solution to the puzzle in the GUI.
