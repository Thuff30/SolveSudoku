#Lists to hold user input
userin0 = (0,0,8,0,0,0,0,0,0)
userin1 = (0,0,0,9,0,1,0,0,0)
userin2 = (0,0,0,0,0,7,2,5,4)
userin3 = (0,3,0,0,0,0,0,2,0)
userin4 = (0,0,0,1,2,0,0,4,6)
userin5 = (0,6,0,0,0,0,5,0,0)
userin6 = (0,0,0,8,0,1,0,0,3)
userin7 = (0,0,0,3,0,0,0,6,0)
userin8 = (0,4,5,0,0,0,8,0,0)

puzzle = [[[0,0],userin0[0],[0,]],[[0,1],userin0[1],[0,]],[[0,2],userin0[2],[0,]],[[0,3],userin0[3],[0,]],[[0,4],userin0[4],[0,]],\
  [[0,5],userin0[5],[0,]],[[0,6],userin0[6],[0,]],[[0,7],userin0[7],[0,]],[[0,8],userin0[8],[0,]],[[1,0],userin1[0],[0,]],\
  [[1,1],userin1[1],[0,]],[[1,2],userin1[2],[0,]],[[1,3],userin1[3],[0,]],[[1,4],userin1[4],[0,]],[[1,5],userin1[5],[0,]],\
  [[1,6],userin1[6],[0,]],[[1,7],userin1[7],[0,]],[[1,8],userin1[8],[0,]],[[2,0],userin2[0],[0,]],[[2,1],userin2[1],[0,]],\
  [[2,2],userin2[2],[0,]],[[2,3],userin2[3],[0,]],[[2,4],userin2[4],[0,]],[[2,5],userin2[5],[0,]],[[2,6],userin2[6],[0,]],\
  [[2,7],userin2[7],[0,]],[[2,8],userin2[8],[0,]],[[3,0],userin3[0],[0,]],[[3,1],userin3[1],[0,]],[[3,2],userin3[2],[0,]],\
  [[3,3],userin3[3],[0,]],[[3,4],userin4[4],[0,]],[[3,5],userin3[5],[0,]],[[3,6],userin3[6],[0,]],[[3,7],userin3[7],[0,]],\
  [[3,8],userin3[8],[0,]],[[4,0],userin4[0],[0,]],[[4,1],userin4[1],[0,]],[[4,2],userin4[2],[0,]],[[4,3],userin4[3],[0,]],\
  [[4,4],userin4[4],[0,]],[[4,5],userin4[5],[0,]],[[4,6],userin4[6],[0,]],[[4,7],userin4[7],[0,]],[[4,8],userin4[8],[0,]],\
  [[5,0],userin5[0],[0,]],[[5,1],userin5[1],[0,]],[[5,2],userin5[2],[0,]],[[5,3],userin5[3],[0,]],[[5,4],userin5[4],[0,]],\
  [[5,5],userin5[5],[0,]],[[5,6],userin5[6],[0,]],[[5,7],userin5[7],[0,]],[[5,8],userin5[8],[0,]],[[6,0],userin6[0],[0,]],\
  [[6,1],userin6[1],[0,]],[[6,2],userin6[2],[0,]],[[6,3],userin6[3],[0,]],[[6,4],userin6[4],[0,]],[[6,5],userin6[5],[0,]],\
  [[6,6],userin6[6],[0,]],[[6,7],userin6[7],[0,]],[[6,8],userin6[8],[0,]],[[7,0],userin7[0],[0,]],[[7,1],userin7[1],[0,]],\
  [[7,2],userin7[2],[0,]],[[7,3],userin7[3],[0,]],[[7,4],userin7[4],[0,]],[[7,5],userin7[5],[0,]],[[7,6],userin7[6],[0,]],\
  [[7,7],userin7[7],[0,]],[[7,8],userin7[8],[0,]],[[8,0],userin8[0],[0,]],[[8,1],userin8[1],[0,]],[[8,2],userin8[2],[0,]],\
  [[8,3],userin8[3],[0,]],[[8,4],userin8[4],[0,]],[[8,5],userin8[5],[0,]],[[8,6],userin8[6],[0,]],[[8,7],userin8[7],[0,]],\
  [[8,8],userin8[8],[0,]]]

def check_definites(puzzle):
  #check for 1s sequentially
  it = 0
  curnum = 1
  check = 1
  locations =[0,]
  for x in puzzle:
    if x[1] == curnum:
      locations.append(x[0])
      print(x[0])
    it+=1
  print(locations)
  while check < len(locations):
    it2 = 0
    # while it2 < 81:
    #   row = locations[check][0]
    #   if row == 0:
    #     for x in locations:
    #       if x[0] == 1 or x[0] == 2:
    #         print(x)
    #         continue
    #       else:

    #   else if row == 1:
    #     for x in locations:
    #       if x[0] == 0 or x[0] == 2:
    #         print(x)
    #         continue
    #       else:

    #   else if row == 2:

    #   else if row == 3:

    #   else if row == 4:

    #   else if row == 5:

    #   else if row == 6:

    #   else if row == 7:

    #   else if row == 8:
    check+=1

check_definites(puzzle)
