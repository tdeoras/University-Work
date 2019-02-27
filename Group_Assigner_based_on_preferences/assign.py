#!/usr/bin/env python2
# put your group assignment problem here!
                                               

#(1) Search Problem:  The search problem is a A* where  heuristic is implemented using the preference of students from the question. Here the start state is a N*3 empty matrix where N is the no of sudents.


#(2) State Space: N= Number of Students; Here all possible states include N,[N*(N-1)], [N*(N-1)*(N-2)] such that all possible combinations of team are considered.


#(3) Successor Function: In the empty matrix of N*3 dimensions, the successor function picks the first name and places it at the first row , first column and then pairs that student with 0,1 & 2 students iteratively.


#(4) Edge weights: Each edge is the computation required for assigning the group in the solution.


#(5) Goal State:Goal state is reached when all names have been exhausted and all the students have been assigned a group.


#(6) Heuristic: Heuristic is based on preferences given by students and the k,m,n values provided in the question.


#(7) Algorithm: The algorithm takes the following path towards execution: It starts with the initial state of N*3 empty matrix and adds the first name in the matrix.Further it pairs that student with multiple combinations 
#of students as given in the state space. Now based on the heuristic each combination with lowest value in terms of minimum amount of work required by the staff is evaluated. Upon finding the right combination the student is
#assigned to the team and that name is removed from the list of students. This process is repeated untill all names have been exhausted from the list and the team combinations/asignments are completed.


#(8) Problems Faced: If the list of names is huge or the students are too picky about their preferences of team mates the time to compute he solution is increased exponentially. As the number of combinations to try are multiple in amount.




from itertools import combinations
import copy
from random import randrange, sample
import sys
import string
import Queue as queue


#Open Files and read Data
fp = open(sys.argv[1])
lines = fp.readlines()
fp.close()
w, h = 4, len(lines);
pref  = [[0 for x in range(w)] for y in range(h)]

for i in range(0,len(lines)):
    hum = lines[i].split()
    for j in range(0,4):
        pref[i][j] = hum[j]

w, h = 3,len(lines)
start  = [[0 for x in range(w)] for y in range(h)]

w = len(lines)
names  = [0 for x in range(w)]
for i in range(0,len(lines)):
    names[i] = pref[i][0]


comb1 = combinations(names,1)

count1 = 0
comb1list = []
for elem in list(comb1):
    comb1list.append(elem)
    count1 = count1 + 1

comb2 = combinations(names,2)

count2 = 0
comb2list = []
for elem in list(comb2):
    comb2list.append(elem)
    count2 = count2 + 1
#Successor Function

def succesor1(current):

   temp_name = copy.deepcopy(names)
   temp_current = copy.deepcopy(current)
   size = len(temp_name)
   for i in range(0,len(lines)):
       for j in range(0,3):
           for s in range(len(temp_name)-1, -1, -1):
               if(temp_name[s] == current[i][j]):
                    temp_name.remove(temp_name[s])

   for p in range(0,len(lines)):
       if(temp_current[p][0] == 0):
           temp_current[p][0] = temp_name[0]
           temp_name.remove(temp_name[0])
           row = p
           break
   comb1 = combinations(temp_name,1)
   count1 = 0
   comb1list = []
   for elem in list(comb1):
       comb1list.append(elem)
       count1 = count1 + 1

   comb2 = combinations(temp_name,2)
   count2 = 0
   comb2list = []
   for elem in list(comb2):
       comb2list.append(elem)
       count2 = count2 + 1

   w = len(comb1list) + len(comb2list) + 1
   succ  = [copy.deepcopy(temp_current) for x in range(w)]
   for k in range(0,len(comb1list)):
       succ[k][row][1] = comb1list[k][0]
   for j in range(0,len(comb2list)):
       succ[len(comb1list) + j][row][1] = comb2list[j][0]
       succ[len(comb1list) + j][row][2] = comb2list[j][1]
   return succ


k = int(sys.argv[2])
not_group = int(sys.argv[3])
yes_group = int(sys.argv[4])

def heuristic(current):
    temp_state = copy.deepcopy(current)
    heu = 0
    for i in range(0,len(lines)):
        if(temp_state[i][0] != 0):
           heu = heu + k

    for i in range(0,len(lines)):
        count = 0
        for j in range(0,3):
            if(temp_state[i][j] != 0):
               count = count + 1
        for n in range(0,3):
            for m in range(0,len(lines)):
                if(temp_state[i][n] == pref[m][0]):
                   if(int(pref[m][1]) != count):
                      heu = heu + 1


    for i in range(0,len(lines)):
        for j in range(0,3):
            if(temp_state[i][j] != 0):
                for m in range(0,len(lines)):
                    if(temp_state[i][j] == pref[m][0]):
                           ywork = pref[m][2].split(',')
                           for elem in ywork:
                               if not (elem in temp_state[i]):
                                    heu = heu + yes_group


    for i in range(0,len(lines)):
        for j in range(0,3):
            if(temp_state[i][j] != 0):
                for m in range(0,len(lines)):
                    if(temp_state[i][j] == pref[m][0]):
                           nwork = pref[m][3].split(',')
                           for elem in nwork:
                               if(elem in temp_state[i]):
                                    heu = heu + not_group


    return heu

def is_goal(state):
    count = 0
    for i in range(0,len(lines)):
       for j in range(0,3):
           if(state[i][j] != 0):
               count = count + 1
    return count == len(names)

def remove_values_from_list(the_list, val):
        while val in the_list:
            the_list.remove(val)


def solve(initial_board):

    fringe = queue.PriorityQueue()
    fringe.put((1000,start))
    while fringe.qsize() > 0:
        (h,state) = fringe.get()
        for (succ) in succesor1( state ):
                if is_goal(succ):
                    count = 0
                    temp = []
                    for m in range(0,len(lines)):
                        if(succ[m][0] != 0):
                          count = count + 1
                    w, h = 3, count;
                    temp  = [[0 for x in range(w)] for y in range(h)]
                    for i in range(0,count):
                        for j in range(0,3):
                            if succ[i][j] != 0:
                               temp[i][j] = succ[i][j]
                    for i in range(0,count):
                        if 0 in temp[i]:
                           remove_values_from_list(temp[i],0)
#                    print temp
                    print('\n'.join(' '.join(str(x) for x in row) for row in temp))
                    print heuristic(succ)
                    return succ
                heu = heuristic(succ)
                fringe.put((heu,succ))

    return False





solve(start)

   


  
