#!/usr/bin/env python2                                                                                                                                                                           
import sys
import numpy as np

#Count if piece present on row

def count_on_row(board, row):
     return sum( board[row] )

#Count if piece present on collumn

def count_on_col(board, col):
     return sum( [ row[col] for row in board ] )

#Count if piece present on diagonal
#Refered from : https://codereview.stackexchange.com/questions/146935/find-diagonal-positions-for-bishop-movement
def count_on_diagonals(coord, size, board):
    limit = size - 1
    coords = [coord]
    row = coord[0]
    col = coord[1]

    while row > 0 and col > 0:
        row -= 1
        col -= 1
        coords.append((row, col))

    row = coord[0]
    col = coord[1]

    while row < limit and col < limit:
        row += 1
        col += 1
        coords.append((row, col))

    row = coord[0]
    col = coord[1]

    while row < limit and col > 0:
        row += 1
        col -= 1
        coords.append((row, col))

    row = coord[0]
    col = coord[1]

    while row > 0 and col < limit:
        row -= 1
        col += 1
        coords.append((row, col))

    list1, list2 = zip(*coords)
    sum = 0
    for f, b in zip(list1, list2):
        sum += board[f][b]
    return sum

#Count if piece present on Board
def count_pieces(board):
     return sum([ sum(row) for row in board ] )

#Print board for rooks      

def printable_board(board):
     return "\n".join([ " ".join([ "R" if col == 1  else "X" if col == 99  else "_" for col in row ]) for row in board])

#Print board for queen  

def printable_board_queen(board):
     return "\n".join([ " ".join([ "Q" if col == 1  else "X" if col == 99  else "_" for col in row ]) for row in board])

#Add piece on board

def add_piece(board, row, col):
     return board[0:row] + [board[row][0:col] + [1,] + board[row][col+1:]] + board[row+1:]

#Marking place where piece is not allowed 

def add_piece_blank(board, row, col):
     return board[0:row] + [board[row][0:col] + [99,] + board[row][col+1:]] + board[row+1:]

#Basic sucessor

def successors(board):
    return [ add_piece(board, r, c) for r in range(0, N) for c in range(0,N) ]

#Check if state is goal
def is_goal(board):
     return count_pieces(board) == N and \
         all( [ count_on_row(board, r) <= 1 for r in range(0, N) ] ) and \
         all( [ count_on_col(board, c) <= 1 for c in range(0, N) ] )

#Sucessor sates for nrook where there is check for N and if pieces are attacked through row or collumn

def successors7(board):
 result = []
 if(count_pieces(board) < N):
    for j in range(0,N):
        if(count_on_col(board,j) == 0):
             collumn = j
             break

    for i in range(0,N):
      if(count_on_row(board,i) == 0):
        if(npos == 0):
           result.append(add_piece(board,i,collumn))
        else:
           flag = 0
           for p in range(4,4+(npos*2),2):
               if ((i == int(sys.argv[p]) - 1 and collumn == int(sys.argv[p+1]) - 1)):
                   flag = 1
           if(flag != 1):
                 result.append(add_piece(board,i,collumn))

 return result

 #Sucessor sates for nqueen where there is check for N and if pieces are attacked through row or collumn or diagonal

def successors8(board):
 result = []
 if(count_pieces(board) < N):
    for j in range(0,N):
        if(count_on_col(board,j) == 0):
             collumn = j
             break

    for i in range(0,N):
      if(count_on_row(board,i) == 0 and count_on_diagonals((i,collumn),N,board) == 0):
        if(npos == 0):
           result.append(add_piece(board,i,collumn))
        else:
           flag = 0
           for p in range(4,4+(npos*2),2):
               if ((i == int(sys.argv[p]) - 1 and collumn == int(sys.argv[p+1]) - 1)):
                   flag = 1
           if(flag != 1):
                      result.append(add_piece(board,i,collumn))

 return result

def solve(initial_board):
    fringe = [initial_board]
    while len(fringe) > 0:
       if(choice == "nrook"):
             for s in (successors7( fringe.pop() ) ) :
               if is_goal(s):
                   return(s)
               fringe.append(s)
       if(choice == "nqueen"):
             for s in (successors8( fringe.pop() ) ) :
               if is_goal(s):
                   return(s)
               fringe.append(s)
    return False

N = int(sys.argv[2])
choice = str(sys.argv[1])
npos = int(sys.argv[3])
initial_board = [[0]*N]*N
print ("Starting from initial board:\n" + printable_board(initial_board) + "\n\nLooking for solution...\n")
solution = solve(initial_board)
for p in range(4,4+(npos*2),2):
  solution = add_piece_blank(solution,int(sys.argv[p]) - 1,int(sys.argv[p+1]) - 1)
if(choice == "nrook"):
   print printable_board(solution) if solution else "Sorry, no solution found. :("
else:
   print printable_board_queen(solution) if solution else "Sorry, no solution found. :("