#!/usr/bin/env python2 
# Design Decisions
# Heuristic : Heuristic tries to maximize the pieces of that particular player on top n rows
# Min-Max : Min-Max algorithm has been used 
# IDS : Iterative deepening search has been used to move down the tree(depth:100)
# No Time Constrain : No time constrain has been taken.Instead the program prints move iteratively as it goes down the depth
# Dynamic Tree : Tree has been built dynamically to avoid recomputations 

from itertools import combinations
import copy
from random import randrange, sample
import sys
import string
import Queue as queue
import sys
import time


n = int(sys.argv[1])
initial = sys.argv[3]
minutes = int(sys.argv[4])
move_person = sys.argv[2]
temp_n = n


# print initial                                                                                                                                                                                             


# n = 3                                                                                                                                                                                                     

start  = [[0 for x in range(n)] for y in range(n+3)]

count = 0
for i in range(n+3-1,-1,-1):
    for j in range(0,n):
        start[i][j] = initial[count]
        count = count + 1

#print start                                                                                                                                                                                                

#start[5][0] = 'x'                                                                                                                                                                                          
#print start                                                                                                                                                                                                
#test = [['x', 'o', 'x'], ['x', 'x', 'x'], ['o', 'o', 'o'], ['x', 'x', '.'], ['.', '.', '.'], ['.', '.', '.']]                                                                                              

# move_person = 'o'                             

#Successor Function
def succesor(state):
    result = []
    if move_person == 'x':
       mv = 'x'
    else:
       mv = 'o'
    for i in range(0,n):
        flag = 0
        for j in range(0,n+3):
            if(state[j][i] == '.'):
               flag = 1
            if flag == 1:
               succ = copy.deepcopy(state)
               succ[j][i] = mv
               result.append((i+1,succ))
#               print 'Inside'                                                                                                                                                                              
               break

#        print result                                                                                                                                                                                       

    for i in range(0,n):
        succ = copy.deepcopy(state)
        for m in range(n+3-1,-1,-1):
            if(succ[m][i] != '.'):
              top = m
              top_elem = succ[m][i]
#              print top,top_elem,m,i                                                                                                                                                                       
              break
            elif(succ[0][i] == '.'):
              top = 0
              top_elem = succ[0][i]
              break
        temp = succ[0][i]
        for j in range(0,n+3-1):
            succ[j][i] = state[j+1][i]

        succ[top][i] = temp
        result.append((-(i+1),succ))

#    for elem in result:                                                                                                                                                                                    
#        print '\n'                                                                                                                                                                                         
#        for elem1 in elem[1]:                                                                                                                                                                              
#            print elem1                                                                                                                                                                                    
#            print '\n'                                                                                                                                                                                     

    return result
# Check Goal State
def is_goal(state):
    succ = copy.deepcopy(state)
    for i in range(n,n+3):
        if all(succ[i][j] == 'x' for j in range(0,n)) is True:
           return True
        if all(succ[i][j] == 'o' for j in range(0,n)) is True:
           return True
    for j in range(0,n):
               if all(succ[i][j] == 'x' for i in range(n,n+3)) is True:
                  return True
               if all(succ[i][j] == 'o' for i in range(n,n+3)) is True:
                  return True
    if all(succ[i][i-n] == 'x' for i in range(n,n+3)) is True:
       return True
    if all(succ[i][i-n] == 'o' for i in range(n,n+3)) is True:
       return True
    if all(succ[n+3-1-i][i] == 'x' for i in range(n-1,-1,-1)) is True:
       return True
    if all(succ[n+3-1-i][i] == 'o' for i in range(0,n)) is True:
       return True
    return False

def heuristic(state):
    xcount = 0
    ycount = 0
    for i in range(3,n+3):
        for j in range(0,n):
            if(state[i][j] == 'x'):
               xcount = xcount + 1
            if(state[i][j] == 'o'):
               ycount = ycount + 1
    return xcount - ycount


class Node(object):
    def __init__(self, data):
        self.data = data
        self.children = []
        self.father_i = -1
        self.father_k = -1
        self.current_max = -1000
        self.current_min = 1000
        self.move = 0

    def add_child(self, obj):
        self.children.append(obj)

#p = Node(test)                                                                                                                                                                                             
#for succ in succesor(test):                                                                                                                                                                                
#    p.add_child(succ[1])                                                                                                                                                                                   

#for c in p.children:                                                                                                                                                                                       
#    print c                                                                                                                                                                                                

# Building Trees Dynamically

def solve(state):
#    level  = [[0 for x in range(0,10)] for y in range(0,10)]                                                                                                                                               
#    print state                                                                                                                                                                                            
#    level[0][0] = Node(state)                                                                                                                                                                              
#   print level[0][0].data                                                                                                                                                                                  
#    print level[0]                                                                                                                                                                                         
    global move_person
    global temp_n
    temp_person = move_person
    for i in range(2,100,2):
        level  = [[0 for x in range(0,10)] for y in range(0,10)]
        level[0][0] = Node(state)
        for j in range(0,i,1):
            if j%2 == 0:
               move_person = 'x'
            else:
               move_person = 'o'
#            print level[j]                                                                                                                                                                                 
            count = 0
            for elem in level[j]:
                count = count + 1
                if elem != 0:
#                   print elem.data                                                                                                                                                                         
                   for succ in succesor(elem.data):
#                       print succ                                                                                                                                                                          
                       p = Node(succ[1])
                       p.father_i = j
                       p.father_k = count-1
                       p.move = succ[0]
                       elem.add_child(p)
                       level[j+1].append(p)
        if temp_person == 'x':
           for elem in level[i]:
               if elem!= 0:
                  elem.current_max = heuristic(elem.data)
        else:
           for elem in level[i]:
               if elem!= 0:
                  elem.current_min = heuristic(elem.data)

        if temp_person == 'x':
           for m in range(i,0,-1):
                 for elem in level[m]:
                    if elem != 0:
                       if m%2 == 0:
                          if level[elem.father_i][elem.father_k].current_min > elem.current_max:
                             level[elem.father_i][elem.father_k].current_min = elem.current_max
                       else:
                          if level[elem.father_i][elem.father_k].current_max < elem.current_min:
                             level[elem.father_i][elem.father_k].current_max = elem.current_min

        else:
           for m in range(i,0,-1):
                 for elem in level[m]:
                    if elem != 0:
                       if m%2 == 0:
                          if level[elem.father_i][elem.father_k].current_max < elem.current_min:
                             level[elem.father_i][elem.father_k].current_max = elem.current_min
                       else:
                          if level[elem.father_i][elem.father_k].current_min > elem.current_max:
                             level[elem.father_i][elem.father_k].current_min = elem.current_max

        if temp_person == 'x':
           find = level[0][0].current_max
           for elem in level[1]:
               if elem!=0 and elem.current_min == find:
#                  print elem.data                                                                                                                                                                          
#                  print 'Move:'                                                                                                                                                                            
#                  print elem.move                                                                                                                                                                          
#                  print elem.move,                                                                                                                                                                         

                  str = ''
                  for i in range(temp_n+3-1,-1,-1):
                      for j in range(0,n):
                          str = str + elem.data[i][j]
                  print elem.move,
                  print str.replace(" ", "")
                  break
        else:
           find = level[0][0].current_min
           for elem in level[1]:
               if elem!=0 and elem.current_max == find:
#                  print elem.data                                                                                                                                                                          
#                  print 'Move:'                                                                                                                                                                            
#                  print elem.move,                                                                                                                                                                         
#                  print ' ',                                                                                                                                                                               
                  str = ''
                  for i in range(temp_n+3-1,-1,-1):
                      for j in range(0,n):
                          str = str + elem.data[i][j]
                  print elem.move,
                  print str.replace(" ", "")
                  break


#    for elem in level[4]:                                                                                                                                                                                  
#        if elem!=0:                                                                                                                                                                                        
#           print elem.data,elem.current                                                                                                                                                                    







solve(start)

        

     
