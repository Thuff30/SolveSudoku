import numpy as np

puzzle = [[3,7,0,0,5,0,2,0,0],\
  [4,0,0,7,0,6,0,1,0],\
  [0,0,1,0,0,0,0,0,0],\
  [0,0,0,1,7,0,6,4,0],\
  [0,0,0,0,0,9,0,0,0],\
  [0,9,0,0,0,0,3,0,5],\
  [0,0,0,0,2,0,0,0,0],\
  [0,5,7,8,0,0,0,0,4],\
  [0,0,0,0,0,0,0,8,0]]

def reviewpossibles(y,x,n):
  global puzzle
  for i in range(0,9):
    if puzzle[y][i] == n:
      return False
  for i in range(0,9):
    if puzzle[i][x] == n:
      return False
  x0 = (x//3)*3
  y0 = (y//3)*3
  for a in range(0,3):
    for b in range(0,3):
      if puzzle[y0+a][x0+b] == n:
        return False
  return True

def solve():
  global puzzle
  for y in range(9):
    for x in range(9):
      if puzzle[y][x] == 0:
        for n in range (1,10):
          if reviewpossibles(y,x,n):
            puzzle[y][x] = n
            solve()
            puzzle[y][x] = 0
        return
  print(np.matrix(puzzle))

solve()
