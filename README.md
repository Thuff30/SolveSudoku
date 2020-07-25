This is a simple, barebones Python application that can solve Sudoku puzzles. It has been tested successfully using a variety of difficulty puzzles from varied sources.
The puzzle is solved using 3 functions that implement for loops, recursion, and backtracking. Recursion, if used correctly, helps to minimize excess code by reusing the
existing lines. Backtracking helps to reduce excess code by resetting answers that do not work without the need for extra functions and duplicate lists.

The functions used are input_to_list, reviewpossibles, and solvepuzzle. input_to_list converts the user's input into a list of integers and returns the converted list.
reviewpossibles examines a square in the Sudoku puzzle that is passed into it. It cycles through each possible number (1-9) and checks them against the other squares in 
the same row and column to determine if they are a viable answer. solvepuzzle if fairly self explanatory in that it cycles through every position in the Sudoku puzzle 
and passes them into the reviewpossibles puzzle. This function is where the recursion and backtracking occur.

In the near future this application will include a UI to improve ease of use for the average user.
