import numpy as np
import tkinter as tk
from tkinter import *
from tkinter import messagebox

#function to solve each square
def reviewpossibles(y,x,n):
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

#Function to display the answer to the puzzle
def show_solution():
  #display answers for row0
  row0column0_entry.insert(0,puzzle[0][0])
  row0column1_entry.insert(0,puzzle[0][1])
  row0column2_entry.insert(0,puzzle[0][2])
  row0column3_entry.insert(0,puzzle[0][3])
  row0column4_entry.insert(0,puzzle[0][4])
  row0column5_entry.insert(0,puzzle[0][5])
  row0column6_entry.insert(0,puzzle[0][6])
  row0column7_entry.insert(0,puzzle[0][7])
  row0column8_entry.insert(0,puzzle[0][8])
  #display answers for row1
  row1column0_entry.insert(0,puzzle[1][0])
  row1column1_entry.insert(0,puzzle[1][1])
  row1column2_entry.insert(0,puzzle[1][2])
  row1column3_entry.insert(0,puzzle[1][3])
  row1column4_entry.insert(0,puzzle[1][4])
  row1column5_entry.insert(0,puzzle[1][5])
  row1column6_entry.insert(0,puzzle[1][6])
  row1column7_entry.insert(0,puzzle[1][7])
  row1column8_entry.insert(0,puzzle[1][8])
  #display answers for row2
  row2column0_entry.insert(0,puzzle[2][0])
  row2column1_entry.insert(0,puzzle[2][1])
  row2column2_entry.insert(0,puzzle[2][2])
  row2column3_entry.insert(0,puzzle[2][3])
  row2column4_entry.insert(0,puzzle[2][4])
  row2column5_entry.insert(0,puzzle[2][5])
  row2column6_entry.insert(0,puzzle[2][6])
  row2column7_entry.insert(0,puzzle[2][7])
  row2column8_entry.insert(0,puzzle[2][8])
  #display answers for row3
  row3column0_entry.insert(0,puzzle[3][0])
  row3column1_entry.insert(0,puzzle[3][1])
  row3column2_entry.insert(0,puzzle[3][2])
  row3column3_entry.insert(0,puzzle[3][3])
  row3column4_entry.insert(0,puzzle[3][4])
  row3column5_entry.insert(0,puzzle[3][5])
  row3column6_entry.insert(0,puzzle[3][6])
  row3column7_entry.insert(0,puzzle[3][7])
  row3column8_entry.insert(0,puzzle[3][8])
  #display answers for row4
  row4column0_entry.insert(0,puzzle[4][0])
  row4column1_entry.insert(0,puzzle[4][1])
  row4column2_entry.insert(0,puzzle[4][2])
  row4column3_entry.insert(0,puzzle[4][3])
  row4column4_entry.insert(0,puzzle[4][4])
  row4column5_entry.insert(0,puzzle[4][5])
  row4column6_entry.insert(0,puzzle[4][6])
  row4column7_entry.insert(0,puzzle[4][7])
  row4column8_entry.insert(0,puzzle[4][8])
  #display answers for row5
  row5column0_entry.insert(0,puzzle[5][0])
  row5column1_entry.insert(0,puzzle[5][1])
  row5column2_entry.insert(0,puzzle[5][2])
  row5column3_entry.insert(0,puzzle[5][3])
  row5column4_entry.insert(0,puzzle[5][4])
  row5column5_entry.insert(0,puzzle[5][5])
  row5column6_entry.insert(0,puzzle[5][6])
  row5column7_entry.insert(0,puzzle[5][7])
  row5column8_entry.insert(0,puzzle[5][8])
  #display answers for row6
  row6column0_entry.insert(0,puzzle[6][0])
  row6column1_entry.insert(0,puzzle[6][1])
  row6column2_entry.insert(0,puzzle[6][2])
  row6column3_entry.insert(0,puzzle[6][3])
  row6column4_entry.insert(0,puzzle[6][4])
  row6column5_entry.insert(0,puzzle[6][5])
  row6column6_entry.insert(0,puzzle[6][6])
  row6column7_entry.insert(0,puzzle[6][7])
  row6column8_entry.insert(0,puzzle[6][8])
  #display answers for row7
  row7column0_entry.insert(0,puzzle[7][0])
  row7column1_entry.insert(0,puzzle[7][1])
  row7column2_entry.insert(0,puzzle[7][2])
  row7column3_entry.insert(0,puzzle[7][3])
  row7column4_entry.insert(0,puzzle[7][4])
  row7column5_entry.insert(0,puzzle[7][5])
  row7column6_entry.insert(0,puzzle[7][6])
  row7column7_entry.insert(0,puzzle[7][7])
  row7column8_entry.insert(0,puzzle[7][8])
  #display answers for row8
  row8column0_entry.insert(0,puzzle[8][0])
  row8column1_entry.insert(0,puzzle[8][1])
  row8column2_entry.insert(0,puzzle[8][2])
  row8column3_entry.insert(0,puzzle[8][3])
  row8column4_entry.insert(0,puzzle[8][4])
  row8column5_entry.insert(0,puzzle[8][5])
  row8column6_entry.insert(0,puzzle[8][6])
  row8column7_entry.insert(0,puzzle[8][7])
  row8column8_entry.insert(0,puzzle[8][8])
  
  #notify user
  notice.pack()

#function to solve puzzle
def solvepuzzle():
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
  show_solution()

#Establish main window
root = tk.Tk()
root.title("Sudoku Solver")
root.geometry('500x700')

#Establish frames to hold cells
mainbox = Frame(root, bd = 3)
box0 = Frame(mainbox, bd = 3)
box1 = Frame(mainbox, bd = 3)
box2 = Frame(mainbox, bd = 3)
box3 = Frame(mainbox, bd = 3)
box4 = Frame(mainbox, bd = 3)
box5 = Frame(mainbox, bd = 3)
box6 = Frame(mainbox, bd = 3)
box7 = Frame(mainbox, bd = 3)
box8 = Frame(mainbox, bd = 3)

#Establish labels
notice = Label(root, fg = 'red', font = ('arial', 32, 'bold'),text = "Your puzzle has been solved!", wraplength = 475)
intro = Label(root, font = ('arial', 30, 'bold'),text = "Please fill in all fields, using 0s to represent unknown squares.", wraplength = 475)

#Establish entries for row0
row0column0_entry = Entry(box0, width = 1, bg = '#afcde3', font = ('arial', 20, 'normal'))
row0column1_entry = Entry(box0, width = 1, bg = '#afcde3', font = ('arial', 20, 'normal'))
row0column2_entry = Entry(box0, width = 1, bg = '#afcde3', font = ('arial', 20, 'normal'))
row0column3_entry = Entry(box1, width = 1, font = ('arial', 20, 'normal'))
row0column4_entry = Entry(box1, width = 1, font = ('arial', 20, 'normal'))
row0column5_entry = Entry(box1, width = 1, font = ('arial', 20, 'normal'))
row0column6_entry = Entry(box2, width = 1, bg = '#afcde3', font = ('arial', 20, 'normal'))
row0column7_entry = Entry(box2, width = 1, bg = '#afcde3', font = ('arial', 20, 'normal'))
row0column8_entry = Entry(box2, width = 1, bg = '#afcde3', font = ('arial', 20, 'normal'))
#Establish entries for row1
row1column0_entry = Entry(box0, width = 1, bg = '#afcde3', font = ('arial', 20, 'normal'))
row1column1_entry = Entry(box0, width = 1, bg = '#afcde3', font = ('arial', 20, 'normal'))
row1column2_entry = Entry(box0, width = 1, bg = '#afcde3', font = ('arial', 20, 'normal'))
row1column3_entry = Entry(box1, width = 1, font = ('arial', 20, 'normal'))
row1column4_entry = Entry(box1, width = 1, font = ('arial', 20, 'normal'))
row1column5_entry = Entry(box1, width = 1, font = ('arial', 20, 'normal'))
row1column6_entry = Entry(box2, width = 1, bg = '#afcde3', font = ('arial', 20, 'normal'))
row1column7_entry = Entry(box2, width = 1, bg = '#afcde3', font = ('arial', 20, 'normal'))
row1column8_entry = Entry(box2, width = 1, bg = '#afcde3', font = ('arial', 20, 'normal'))
#Establish entries for row2
row2column0_entry = Entry(box0, width = 1, bg = '#afcde3', font = ('arial', 20, 'normal'))
row2column1_entry = Entry(box0, width = 1, bg = '#afcde3', font = ('arial', 20, 'normal'))
row2column2_entry = Entry(box0, width = 1, bg = '#afcde3', font = ('arial', 20, 'normal'))
row2column3_entry = Entry(box1, width = 1, font = ('arial', 20, 'normal'))
row2column4_entry = Entry(box1, width = 1, font = ('arial', 20, 'normal'))
row2column5_entry = Entry(box1, width = 1, font = ('arial', 20, 'normal'))
row2column6_entry = Entry(box2, width = 1, bg = '#afcde3', font = ('arial', 20, 'normal'))
row2column7_entry = Entry(box2, width = 1, bg = '#afcde3', font = ('arial', 20, 'normal'))
row2column8_entry = Entry(box2, width = 1, bg = '#afcde3', font = ('arial', 20, 'normal'))
#Establish entries for row3
row3column0_entry = Entry(box3, width = 1, font = ('arial', 20, 'normal'))
row3column1_entry = Entry(box3, width = 1, font = ('arial', 20, 'normal'))
row3column2_entry = Entry(box3, width = 1, font = ('arial', 20, 'normal'))
row3column3_entry = Entry(box4, bg = '#afcde3', width = 1, font = ('arial', 20, 'normal'))
row3column4_entry = Entry(box4, bg = '#afcde3', width = 1, font = ('arial', 20, 'normal'))
row3column5_entry = Entry(box4, bg = '#afcde3', width = 1, font = ('arial', 20, 'normal'))
row3column6_entry = Entry(box5, width = 1, font = ('arial', 20, 'normal'))
row3column7_entry = Entry(box5, width = 1, font = ('arial', 20, 'normal'))
row3column8_entry = Entry(box5, width = 1, font = ('arial', 20, 'normal'))
#Establish entries for row4
row4column0_entry = Entry(box3, width = 1, font = ('arial', 20, 'normal'))
row4column1_entry = Entry(box3, width = 1, font = ('arial', 20, 'normal'))
row4column2_entry = Entry(box3, width = 1, font = ('arial', 20, 'normal'))
row4column3_entry = Entry(box4, width = 1, bg = '#afcde3', font = ('arial', 20, 'normal'))
row4column4_entry = Entry(box4, width = 1, bg = '#afcde3', font = ('arial', 20, 'normal'))
row4column5_entry = Entry(box4, width = 1, bg = '#afcde3', font = ('arial', 20, 'normal'))
row4column6_entry = Entry(box5, width = 1, font = ('arial', 20, 'normal'))
row4column7_entry = Entry(box5, width = 1, font = ('arial', 20, 'normal'))
row4column8_entry = Entry(box5, width = 1, font = ('arial', 20, 'normal'))
#Establish entries for row5
row5column0_entry = Entry(box3, width = 1, font = ('arial', 20, 'normal'))
row5column1_entry = Entry(box3, width = 1, font = ('arial', 20, 'normal'))
row5column2_entry = Entry(box3, width = 1, font = ('arial', 20, 'normal'))
row5column3_entry = Entry(box4, width = 1, bg = '#afcde3', font = ('arial', 20, 'normal'))
row5column4_entry = Entry(box4, width = 1, bg = '#afcde3', font = ('arial', 20, 'normal'))
row5column5_entry = Entry(box4, width = 1, bg = '#afcde3', font = ('arial', 20, 'normal'))
row5column6_entry = Entry(box5, width = 1, font = ('arial', 20, 'normal'))
row5column7_entry = Entry(box5, width = 1, font = ('arial', 20, 'normal'))
row5column8_entry = Entry(box5, width = 1, font = ('arial', 20, 'normal'))
#Establish entries for row6
row6column0_entry = Entry(box6, width = 1, bg = '#afcde3', font = ('arial', 20, 'normal'))
row6column1_entry = Entry(box6, width = 1, bg = '#afcde3', font = ('arial', 20, 'normal'))
row6column2_entry = Entry(box6, width = 1, bg = '#afcde3', font = ('arial', 20, 'normal'))
row6column3_entry = Entry(box7, width = 1, font = ('arial', 20, 'normal'))
row6column4_entry = Entry(box7, width = 1, font = ('arial', 20, 'normal'))
row6column5_entry = Entry(box7, width = 1, font = ('arial', 20, 'normal'))
row6column6_entry = Entry(box8, width = 1, bg = '#afcde3', font = ('arial', 20, 'normal'))
row6column7_entry = Entry(box8, width = 1, bg = '#afcde3', font = ('arial', 20, 'normal'))
row6column8_entry = Entry(box8, width = 1, bg = '#afcde3', font = ('arial', 20, 'normal'))
#Establish entries for row7
row7column0_entry = Entry(box6, width = 1, bg = '#afcde3', font = ('arial', 20, 'normal'))
row7column1_entry = Entry(box6, width = 1, bg = '#afcde3', font = ('arial', 20, 'normal'))
row7column2_entry = Entry(box6, width = 1, bg = '#afcde3', font = ('arial', 20, 'normal'))
row7column3_entry = Entry(box7, width = 1, font = ('arial', 20, 'normal'))
row7column4_entry = Entry(box7, width = 1, font = ('arial', 20, 'normal'))
row7column5_entry = Entry(box7, width = 1, font = ('arial', 20, 'normal'))
row7column6_entry = Entry(box8, width = 1, bg = '#afcde3', font = ('arial', 20, 'normal'))
row7column7_entry = Entry(box8, width = 1, bg = '#afcde3', font = ('arial', 20, 'normal'))
row7column8_entry = Entry(box8, width = 1, bg = '#afcde3', font = ('arial', 20, 'normal'))
#Establish entries for row8
row8column0_entry = Entry(box6, width = 1, bg = '#afcde3', font = ('arial', 20, 'normal'))
row8column1_entry = Entry(box6, width = 1, bg = '#afcde3', font = ('arial', 20, 'normal'))
row8column2_entry = Entry(box6, width = 1, bg = '#afcde3', font = ('arial', 20, 'normal'))
row8column3_entry = Entry(box7, width = 1, font = ('arial', 20, 'normal'))
row8column4_entry = Entry(box7, width = 1, font = ('arial', 20, 'normal'))
row8column5_entry = Entry(box7, width = 1, font = ('arial', 20, 'normal'))
row8column6_entry = Entry(box8, width = 1, bg = '#afcde3', font = ('arial', 20, 'normal'))
row8column7_entry = Entry(box8, width = 1, bg = '#afcde3', font = ('arial', 20, 'normal'))
row8column8_entry = Entry(box8, width = 1, bg = '#afcde3', font = ('arial', 20, 'normal'))

#Add entries to box0
row0column0_entry.grid(row = 0, column = 0)
row0column1_entry.grid(row = 0, column = 1)
row0column2_entry.grid(row = 0, column = 2)
row1column0_entry.grid(row = 1, column = 0)
row1column1_entry.grid(row = 1, column = 1)
row1column2_entry.grid(row = 1, column = 2)
row2column0_entry.grid(row = 2, column = 0)
row2column1_entry.grid(row = 2, column = 1)
row2column2_entry.grid(row = 2, column = 2)
#Add entries to box1
row0column3_entry.grid(row = 0, column = 0)
row0column4_entry.grid(row = 0, column = 1)
row0column5_entry.grid(row = 0, column = 2)
row1column3_entry.grid(row = 1, column = 0)
row1column4_entry.grid(row = 1, column = 1)
row1column5_entry.grid(row = 1, column = 2)
row2column3_entry.grid(row = 2, column = 0)
row2column4_entry.grid(row = 2, column = 1)
row2column5_entry.grid(row = 2, column = 2)
#Add entries to box2
row0column6_entry.grid(row = 0, column = 0)
row0column7_entry.grid(row = 0, column = 1)
row0column8_entry.grid(row = 0, column = 2)
row1column6_entry.grid(row = 1, column = 0)
row1column7_entry.grid(row = 1, column = 1)
row1column8_entry.grid(row = 1, column = 2)
row2column6_entry.grid(row = 2, column = 0)
row2column7_entry.grid(row = 2, column = 1)
row2column8_entry.grid(row = 2, column = 2)
#Add entries to box3
row3column0_entry.grid(row = 0, column = 0)
row3column1_entry.grid(row = 0, column = 1)
row3column2_entry.grid(row = 0, column = 2)
row4column0_entry.grid(row = 1, column = 0)
row4column1_entry.grid(row = 1, column = 1)
row4column2_entry.grid(row = 1, column = 2)
row5column0_entry.grid(row = 2, column = 0)
row5column1_entry.grid(row = 2, column = 1)
row5column2_entry.grid(row = 2, column = 2)
#Add entries to box4
row3column3_entry.grid(row = 0, column = 0)
row3column4_entry.grid(row = 0, column = 1)
row3column5_entry.grid(row = 0, column = 2)
row4column3_entry.grid(row = 1, column = 0)
row4column4_entry.grid(row = 1, column = 1)
row4column5_entry.grid(row = 1, column = 2)
row5column3_entry.grid(row = 2, column = 0)
row5column4_entry.grid(row = 2, column = 1)
row5column5_entry.grid(row = 2, column = 2)
#Add entries to box5
row3column6_entry.grid(row = 0, column = 0)
row3column7_entry.grid(row = 0, column = 1)
row3column8_entry.grid(row = 0, column = 2)
row4column6_entry.grid(row = 1, column = 0)
row4column7_entry.grid(row = 1, column = 1)
row4column8_entry.grid(row = 1, column = 2)
row5column6_entry.grid(row = 2, column = 0)
row5column7_entry.grid(row = 2, column = 1)
row5column8_entry.grid(row = 2, column = 2)
#Add entries to box6
row6column0_entry.grid(row = 0, column = 0)
row6column1_entry.grid(row = 0, column = 1)
row6column2_entry.grid(row = 0, column = 2)
row7column0_entry.grid(row = 1, column = 0)
row7column1_entry.grid(row = 1, column = 1)
row7column2_entry.grid(row = 1, column = 2)
row8column0_entry.grid(row = 2, column = 0)
row8column1_entry.grid(row = 2, column = 1)
row8column2_entry.grid(row = 2, column = 2)
#Add entries to box7
row6column3_entry.grid(row = 0, column = 0)
row6column4_entry.grid(row = 0, column = 1)
row6column5_entry.grid(row = 0, column = 2)
row7column3_entry.grid(row = 1, column = 0)
row7column4_entry.grid(row = 1, column = 1)
row7column5_entry.grid(row = 1, column = 2)
row8column3_entry.grid(row = 2, column = 0)
row8column4_entry.grid(row = 2, column = 1)
row8column5_entry.grid(row = 2, column = 2)
#Add entries to box8
row6column6_entry.grid(row = 0, column = 0)
row6column7_entry.grid(row = 0, column = 1)
row6column8_entry.grid(row = 0, column = 2)
row7column6_entry.grid(row = 1, column = 0)
row7column7_entry.grid(row = 1, column = 1)
row7column8_entry.grid(row = 1, column = 2)
row8column6_entry.grid(row = 2, column = 0)
row8column7_entry.grid(row = 2, column = 1)
row8column8_entry.grid(row = 2, column = 2)

#Add components to main window
intro.pack()
mainbox.pack()
box0.grid(row = 0, column = 0)
box1.grid(row = 0, column = 1)
box2.grid(row = 0, column = 2)
box3.grid(row = 1, column = 0)
box4.grid(row = 1, column = 1)
box5.grid(row = 1, column = 2)
box6.grid(row = 2, column = 0)
box7.grid(row = 2, column = 1)
box8.grid(row = 2, column = 2)

#Clear entire puzzle
def clear_puzzle():
  #Clear row 0
  row0column0_entry.delete(0)
  row0column1_entry.delete(0)
  row0column2_entry.delete(0)
  row0column3_entry.delete(0)
  row0column4_entry.delete(0)
  row0column5_entry.delete(0)
  row0column6_entry.delete(0)
  row0column7_entry.delete(0)
  row0column8_entry.delete(0)
  #Clear row 1
  row1column0_entry.delete(0)
  row1column1_entry.delete(0)
  row1column2_entry.delete(0)
  row1column3_entry.delete(0)
  row1column4_entry.delete(0)
  row1column5_entry.delete(0)
  row1column6_entry.delete(0)
  row1column7_entry.delete(0)
  row1column8_entry.delete(0)
  #Clear row 2
  row2column0_entry.delete(0)
  row2column1_entry.delete(0)
  row2column2_entry.delete(0)
  row2column3_entry.delete(0)
  row2column4_entry.delete(0)
  row2column5_entry.delete(0)
  row2column6_entry.delete(0)
  row2column7_entry.delete(0)
  row2column8_entry.delete(0)
  #Clear row 3
  row3column0_entry.delete(0)
  row3column1_entry.delete(0)
  row3column2_entry.delete(0)
  row3column3_entry.delete(0)
  row3column4_entry.delete(0)
  row3column5_entry.delete(0)
  row3column6_entry.delete(0)
  row3column7_entry.delete(0)
  row3column8_entry.delete(0)
  #Clear row 4
  row4column0_entry.delete(0)
  row4column1_entry.delete(0)
  row4column2_entry.delete(0)
  row4column3_entry.delete(0)
  row4column4_entry.delete(0)
  row4column5_entry.delete(0)
  row4column6_entry.delete(0)
  row4column7_entry.delete(0)
  row4column8_entry.delete(0)
  #Clear row 5
  row5column0_entry.delete(0)
  row5column1_entry.delete(0)
  row5column2_entry.delete(0)
  row5column3_entry.delete(0)
  row5column4_entry.delete(0)
  row5column5_entry.delete(0)
  row5column6_entry.delete(0)
  row5column7_entry.delete(0)
  row5column8_entry.delete(0)
  #Clear row 6
  row6column0_entry.delete(0)
  row6column1_entry.delete(0)
  row6column2_entry.delete(0)
  row6column3_entry.delete(0)
  row6column4_entry.delete(0)
  row6column5_entry.delete(0)
  row6column6_entry.delete(0)
  row6column7_entry.delete(0)
  row6column8_entry.delete(0)
  #Clear row 7
  row7column0_entry.delete(0)
  row7column1_entry.delete(0)
  row7column2_entry.delete(0)
  row7column3_entry.delete(0)
  row7column4_entry.delete(0)
  row7column5_entry.delete(0)
  row7column6_entry.delete(0)
  row7column7_entry.delete(0)
  row7column8_entry.delete(0)
  #Clear row 8
  row8column0_entry.delete(0)
  row8column1_entry.delete(0)
  row8column2_entry.delete(0)
  row8column3_entry.delete(0)
  row8column4_entry.delete(0)
  row8column5_entry.delete(0)
  row8column6_entry.delete(0)
  row8column7_entry.delete(0)
  row8column8_entry.delete(0)
  #Hide completion label
  notice.pack_forget()

#Convert user into to a list of lists and solve the puzzle
def submit_input():
  try:
    line0 = [int(row0column0_entry.get()), int(row0column1_entry.get()), int(row0column2_entry.get()), int(row0column3_entry.get()), int(row0column4_entry.get()), 
      int(row0column5_entry.get()), int(row0column6_entry.get()), int(row0column7_entry.get()), int(row0column8_entry.get())]
    line1 = [int(row1column0_entry.get()), int(row1column1_entry.get()), int(row1column2_entry.get()), int(row1column3_entry.get()), int(row1column4_entry.get()), 
      int(row1column5_entry.get()), int(row1column6_entry.get()), int(row1column7_entry.get()), int(row1column8_entry.get())]
    line2 = [int(row2column0_entry.get()), int(row2column1_entry.get()), int(row2column2_entry.get()), int(row2column3_entry.get()), int(row2column4_entry.get()), 
      int(row2column5_entry.get()), int(row2column6_entry.get()), int(row2column7_entry.get()), int(row2column8_entry.get())]
    line3 = [int(row3column0_entry.get()), int(row3column1_entry.get()), int(row3column2_entry.get()), int(row3column3_entry.get()), int(row3column4_entry.get()), 
      int(row3column5_entry.get()), int(row3column6_entry.get()), int(row3column7_entry.get()), int(row3column8_entry.get())]
    line4 = [int(row4column0_entry.get()), int(row4column1_entry.get()), int(row4column2_entry.get()), int(row4column3_entry.get()), int(row4column4_entry.get()), 
      int(row4column5_entry.get()), int(row4column6_entry.get()), int(row4column7_entry.get()), int(row4column8_entry.get())]
    line5 = [int(row5column0_entry.get()), int(row5column1_entry.get()), int(row5column2_entry.get()), int(row5column3_entry.get()), int(row5column4_entry.get()), 
      int(row5column5_entry.get()), int(row5column6_entry.get()), int(row5column7_entry.get()), int(row5column8_entry.get())]
    line6 = [int(row6column0_entry.get()), int(row6column1_entry.get()), int(row6column2_entry.get()), int(row6column3_entry.get()), int(row6column4_entry.get()), 
      int(row6column5_entry.get()), int(row6column6_entry.get()), int(row6column7_entry.get()), int(row6column8_entry.get())]
    line7 = [int(row7column0_entry.get()), int(row7column1_entry.get()), int(row7column2_entry.get()), int(row7column3_entry.get()), int(row7column4_entry.get()), 
      int(row7column5_entry.get()), int(row7column6_entry.get()), int(row7column7_entry.get()), int(row7column8_entry.get())]
    line8 = [int(row8column0_entry.get()), int(row8column1_entry.get()), int(row8column2_entry.get()), int(row8column3_entry.get()), int(row8column4_entry.get()), 
      int(row8column5_entry.get()), int(row8column6_entry.get()), int(row8column7_entry.get()), int(row8column8_entry.get())]
    #assign user input to list representing the Sudoku puzzle
    global puzzle
    puzzle=[line0, line1, line2, line3, line4, line5, line6, line7, line8]
    solvepuzzle()
  except ValueError:
    messagebox.showerror("Invalid Value", "Please verify all values entered are single digit numbers.")
    clear_puzzle()
    
buttons = Frame(root)
buttons.pack()
submit = tk.Button(buttons, text = "Submit", width = 10, justify = 'center', command = submit_input)
submit.grid(row = 0, column = 0)
reset = Button(buttons, text = "Reset", width = 10, justify = 'center', command = clear_puzzle)
reset.grid(row = 0, column = 1)

root.mainloop()
