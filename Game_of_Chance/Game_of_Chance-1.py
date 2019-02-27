#!/usr/bin/env python2                                                                                                                                                                                      
import sys
import random
import copy
from itertools import combinations
import Queue as queue


# Dice 1,Dice 2,Dice 3
moves = [1,2,3]


# All Possible Combinations in which dice 1,dice 2,dice 3 can be re-rolled
comb1 = combinations(moves,1)
comb2 = combinations(moves,2)
comb3 = combinations(moves,3)

comb1list = []
for elem in list(comb1):
    comb1list.append(elem)

comb2list = []
for elem in list(comb2):
    comb2list.append(elem)

comb3list = []
for elem in list(comb3):
    comb3list.append(elem)


#initial state
s1 = int(sys.argv[1])
s2 = int(sys.argv[2])
s3 = int(sys.argv[3])
start = [0,s1,s2,s3,'']

#Points on a particular state
def heuristic(state):
    if(state[1] == state[2] and state[2] == state[3] and state[3] == state[1]):
          return 25
    else:
          return state[1] + state[2] + state[3]

h = heuristic(start)

#Succesor function which rolls all possible combinations
def sucessor(state):
    result = []
    no_roll = copy.deepcopy(state)
    no_roll[0] = heuristic(no_roll)
    result.append(no_roll)
    for elem in  comb1list:
        for elem1 in elem:
            for i in range(1,7):
                roll = copy.deepcopy(state)
                roll[elem1] = i
                roll[0] = heuristic(roll)
                roll[4] = roll[4] + str(elem1)
                result.append(roll)


    for elem in  comb2list:
            for i in range(1,7):
                for j in range(1,7):
                    roll = copy.deepcopy(state)
                    roll[elem[0]] = i
                    roll[elem[1]] = j
                    roll[0] = heuristic(roll)
                    roll[4] = roll[4] + str(elem[0]) + str(elem[1])
                    result.append(roll)



    for elem in  comb3list:
            for i in range(1,7):
                for j in range(1,7):
                    for k in range(1,7):
                        roll = copy.deepcopy(state)
                        roll[elem[0]] = i
                        roll[elem[1]] = j
                        roll[elem[2]] = k
                        roll[0] = heuristic(roll)
                        roll[4] = roll[4] + str(elem[0]) + str(elem[1]) + str(elem[2])
                        result.append(roll)

    return result

#sucessor([15, 6, 5, 4, '123 '])  

#Maximize function 
#takes into consideration minimum rolls of dices to reach optimal solution
def maximize(state):
    sucessors = sucessor(state)
    fringe = queue.PriorityQueue()
    for succ in sucessors:
            fringe.put((len(succ[4])-succ[0],succ))
    k = fringe.get()[1][4]
    if not k:
       print "DONT ROLL DICE"
    else:
       for elem in k:
           print 'ROLL DICE ' + str(elem)

maximize(start);
