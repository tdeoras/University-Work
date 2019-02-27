#!/usr/bin/env python2                                                                                                                                                                                      
import sys
import numpy as np

def count_on_row(board, row):
     return sum( board[row] )

def count_on_col(board, col):
     return sum( [ row[col] for row in board ] )

def count_pieces(board):
     return sum([ sum(row) for row in board ] )

def printable_board(board):
     return "\n".join([ " ".join([ "R" if col == 1  else "X" if col == 99  else "_" for col in row ]) for row in board])

def add_piece(board, row, col):
     return board[0:row] + [board[row][0:col] + [1,] + board[row][col+1:]] + board[row+1:]

def add_piece_blank(board, row, col):
     return board[0:row] + [board[row][0:col] + [99,] + board[row][col+1:]] + board[row+1:]


#Sucessor sates for nrook where there is check for N and if pieces are attacked through row or collumn - Most efficient

def successors3(board):
  result = []
  if(count_pieces(board) < N):
     for i in range(0,N):
         for j in range(0,N):
             if(count_on_row(board,i) < 1 and count_on_col(board,j) < 1 and board[i][j] != 1):
                 result.append(add_piece(board,i,j))

  return result

def successors(board):
    return [ add_piece(board, r, c) for r in range(0, N) for c in range(0,N) ]


#Adding N and no piece adding issue
#N check is done by counting no of pieces on board during each itertion
#If the position value is 1 that means a piece is already present and that sucessor state is ignored

def successors2(board):
     result = []
     if(count_pieces(board) < N):
        for i in range(0,N):
             for j in range(0,N):
                 if ( board[i][j] != 1 ):
                         result.append(add_piece(board,i,j))
     return result

def successors3(board):
  result = []
  if(count_pieces(board) < N):
     for i in range(0,N):
         for j in range(0,N):
             if(count_on_row(board,i) < 1 and count_on_col(board,j) < 1 and board[i][j] != 1):
                 result.append(add_piece(board,i,j))

  return result

def is_goal(board):
     return count_pieces(board) == N and \
         all( [ count_on_row(board, r) <= 1 for r in range(0, N) ] ) and \
         all( [ count_on_col(board, c) <= 1 for c in range(0, N) ] )


#Code can be changed to BFS by fringe.insert(0,s)
def solve(initial_board):
    fringe = [initial_board]
    while len(fringe) > 0:
             for s in (successors3( fringe.pop() ) ) :
               if is_goal(s):
                   return(s)
               fringe.append(s)
    return False

N = int(sys.argv[1])
initial_board = [[0]*N]*N
print ("Starting from initial board:\n" + printable_board(initial_board) + "\n\nLooking for solution...\n")
solution = solve(initial_board)
print printable_board(solution) if solution else "Sorry, no solution found. :("