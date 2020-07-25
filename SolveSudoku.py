import numpy as np

#function to convert user input to a list of integers
def input_to_list(input):
  listin = input.split(",")
  listout = list(map(int, listin))
  return listout

#function to solve each square
def reviewpossibles(y,x,n):
  global puzzle
  #check column
  for i in range(0,9):
    if puzzle[y][i] == n:
      return False
  #check row
  for i in range(0,9):
    if puzzle[i][x] == n:
      return False
  x2 = (x//3)*3
  y2 = (y//3)*3
  #check square
  for a in range(0,3):
    for b in range(0,3):
      if puzzle[y2+a][x2+b] == n:
        return False
  return True

#function to solve puzzle
def solvepuzzle():
  global puzzle
  #check every square for 0 (blank space)
  for y in range(9):
    for x in range(9):
      if puzzle[y][x] == 0:
        for n in range (1,10):
          if reviewpossibles(y,x,n):
            #enter solution from reviewpossible fucntion
            puzzle[y][x] = n
            #use recursion to recall function until solved
            solvepuzzle()
            #backtracking to reset incorrect answers to 0
            puzzle[y][x] = 0
        return
  #print using numpy for readability
  print(np.matrix(puzzle))

#gather user input
print("Welcome to a simple Sudoku solving application using Python.")
print("When entering the current puzzle, separate each number with a comma (no spaces) and enter a 0 for each blank space.")
user_input = input("Please enter the entire 1st row of the puzzle:")
line0 = input_to_list(user_input)
user_input = input("Please enter the entire 2nd row of the puzzle:")
line1 = input_to_list(user_input)
user_input = input("Please enter the entire 3rd row of the puzzle:")
line2 = input_to_list(user_input)
user_input = input("Please enter the entire 4th row of the puzzle:")
line3 = input_to_list(user_input)
user_input = input("Please enter the entire 5th row of the puzzle:")
line4 = input_to_list(user_input)
user_input = input("Please enter the entire 6th row of the puzzle:")
line5 = input_to_list(user_input)
user_input = input("Please enter the entire 7th row of the puzzle:")
line6 = input_to_list(user_input)
user_input = input("Please enter the entire 8th row of the puzzle:")
line7 = input_to_list(user_input)
user_input = input("Please enter the entire 9th row of the puzzle:")
line8 = input_to_list(user_input)

#assign user input to list representing the Sudoku puzzle
puzzle = [line0, line1, line2, line3, line4, line5, line6, line7, line8]

solvepuzzle()
