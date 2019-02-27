#!/usr/bin/env python2                                                                                                                                                                                        
                                                                                                                                                                                                            
# solver16.py : Circular 16 Puzzle solver                                                                                                                                                                  
                                                                                                                                                                                                            
# Based on skeleton code by D. Crandall, September 2018                                                                                                                                                    


#(1) Search Problem: The solution is based on the implementation of A* Search Algorithm where traversal through the search space is based on finding the path with the lowest cost and only expanding the nodes 
#further for that path.We have tried to come up with a admissible heuristic which is optimal to our case and solves the board configuration to revert to Canonical Configurtion for that board within the puzzle.


#(2) State Space:The state space for the puzzle is all possible combinations that can be expanded , as such the board can have 16! combinations which are included in the search space.


#(3) Successor Function: The successor function expands the states and gives for each state the further possible combinations of traversal. The Successor function in our case has 16 possible moves with L1,L2,L3,L4,
#R1,R2,R3,R4,U1,U2,U3,U4 ,D1,D2,D3,D4  and subsequently the states are expanded based on each move.


#(4) Edge weights: Number of moves where each move represents an individual edge.


#(5) Goal State: The goal state is achieved when the board for the puzzle is organized in the canonical configuration by starting from 1 to 16 with 4 elements in each row and column


#(6) Heuristic & Algorithm: Manhattan Distance is implemented as an admissible heuristic here such we calculate the manhattan distance for each element to it's goal position and only expand states in 
#successor function with lowest manhattan distance.This assures that the goal state is reached in lowest possible time and unneccessary nodes are not expanded leading to excessive time and computation cost in reaching the 
#goal state from the initial board configuration.The heuristic is a round manhattan distance such that the distance between the top and bottom row and left and rigth column is always 1.


#(7) Problems Faced:We faced problem in  board 12 with higher number of moves to reach goal state as too many states are generated. We tried to overcome this problem by limiting the depth of the tree so that if a wrong move
#is expanded the tree is  reverted back and other combinations of moves are tried by further expanding the states within the successor function.
                                                                                                                                                                                                        
                                                                                                                                                                                                            

from random import randrange, sample
import sys
import string
import Queue as queue


#Heuristic Function
def heuristic(state):
    temp = 0
    heu = 0
    w, h = 4, 4;
    nstate = [[0 for x in range(w)] for y in range(h)]
    for i in range(0,4):
        for j in range(0,4):
            nstate[i][j] = state[temp]
            temp = temp + 1
    temp = 1
    for i in range(0,4):
        for j in range(0,4):
            if nstate[i][j] == temp:
               heu = heu + 0
               temp = temp + 1
            else:
               for m in range(0,4):
                   for n in range(0,4):
                       if nstate[m][n] == temp:
                          if(i == 0 and n == j and i + 3 == m):
                                 heu = heu + 1
                          elif(j == 0 and i == m and j + 3 == n):
                                 heu = heu + 1
                          elif(i == 3 and n == j and (i - 3) == m):
                                 heu = heu + 1
                          elif(j == 3 and i == m and j - 3 == n):
                                 heu = heu + 1
                          else:
                                 heu = heu + abs(i-m) + abs(j-n)
               temp = temp + 1
    return heu






# shift a specified row left (1) or right (-1)                                                                                                                                                             
                                                                                                                                                                                                            
def shift_row(state, row, dir):
    change_row = state[(row*4):(row*4+4)]
    return ( state[:(row*4)] + change_row[-dir:] + change_row[:-dir] + state[(row*4+4):], ("L" if dir == -1 else "R") + str(row+1) )

# shift a specified col up (1) or down (-1)                                                                                                                                                                
                                                                                                                                                                                                            
def shift_col(state, col, dir):
    change_col = state[col::4]
    s = list(state)
    s[col::4] = change_col[-dir:] + change_col[:-dir]
    return (tuple(s), ("U" if dir == -1 else "D") + str(col+1) )

# pretty-print board state                                                                                                                                                                                 
                                                                                                                                                                                                            
def print_board(row):
    for j in range(0, 16, 4):
        print '%3d %3d %3d %3d' % (row[j:(j+4)])

# return a list of possible successor states                                                                                                                                                               
                                                                                                                                                                                                            
def successors(state):
    return [ shift_row(state, i, d) for i in range(0,4) for d in (1,-1) ] + [ shift_col(state, i, d) for i in range(0,4) for d in (1,-1) ]

# just reverse the direction of a move name, i.e. U3 -> D3                                                                                                                                                 
                                                                                                                                                                                                            
def reverse_move(state):
    return state.translate(string.maketrans("UDLR", "DURL"))


# check if we've reached the goal                                                                                                                                                                          
                                                                                                                                                                                                            
def is_goal(state):
    return sorted(state) == list(state)

# The solver! - using BFS right now                                                                                                                                                                        
                                                                                                                                                                                                            
def solve(initial_board):
    fringe = queue.PriorityQueue()
    fringe.put((1000,initial_board, ""))
    temp = 18
    count = 0
    while fringe.qsize() > 0:
        (h,state, route_so_far) = fringe.get()
        if(len(route_so_far) >= temp):
            continue
        else:
            for (succ, move) in successors( state ):
                if is_goal(succ):
                    return( route_so_far + " " + move )
                heu = heuristic(succ)
                fringe.put((heu,succ, route_so_far + " " + move ) )

    return False

# test cases                                                                                                                                                                                               
                                                                                                                                                                                                            
start_state = []
with open(sys.argv[1], 'r') as file:
    for line in file:
        start_state += [ int(i) for i in line.split() ]

if len(start_state) != 16:
    print "Error: couldn't parse start state file"

print "Start state: "
print_board(tuple(start_state))


print "Solving..."
route = solve(tuple(start_state))

print "Solution found in " + str(len(route)/3) + " moves:" + "\n" + route
