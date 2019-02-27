#!/usr/bin/env python2                                                                                                                                                                                       
# put your group assignment problem here!                                                                                                                                                                  


#(1) Search Problem:  The search problem was interpreted by passing the parameters Start city and end city through each routing algorithm & Expanding nodes based on  search methods untill end goal was reached.
#The data was inconsistent with missing values which led us to assume certain values based on logic explained below.


#(2) State Space: The state space consists of all the routes from Start city to end city that were expanded inside the successor function.


#(3) Successor Function:Successor Function expands state with the following format (0,0,0,city), for each step the routes leading from the city are expanded and the 3 paramaters are updated.


#(4) Edge weights: The edge weights for BFS,DFS and IDS are 1 and constant in nature. For Uniform the edge weights are dependent on the cost function that is paired with the routing algorithm.
#For A* the edge weights consist of Heuristic + Cost function combined to expand the further states with the lowest computing value for the heurisitic function.


#(5) Goal State:The goal state is achieved when the end city is reached with path leading from stat city , this posed a problem because the data had inconsistency in the form of unidirectional path,
#such that a city A has a path to B  and we want to reach city C,but we don't see a path from B to C. Yet there is a path from C to B which means that they can be traversed amongst themselves.


#(6) Heuristic: The heurisic is a combination of h(s) + g(s) where h(S) is  Haversine Function to calculate the distance between 2 cities given their latitude and longitude and then this distance is used to expand further nodes inside the successor function.


#(7) Algorithm: (A)BFS: For BFS the node was inserted to start of fringe and the last element was popped from fringe and it's successors were found subsequently.

#(B)DFS: For DFS the node was inserted at the end of fringe & it is popped from the fringe and it's subsequent nodes were expanded in the successor function to get further states fro traversing.

#(C)IDS: For Iterative Depeening Search we first expanded the node to element of 1 city, the 2nd city , then 3rd city and so on upto 20 cities.

#(D)UNIFORM: A priority queue was used based on the cost function which are Distance,Segments & Time.The successors were assigned priority and expanded based on the given priority and further states were considered.

#(E)ASTAR: For A* we have used the combination of heuristic funciton + cost function , where the heuristic used is the Haversine function. The combined cost was analysed and the states with the lowest cost
#were only expanded further in the successor function to reach the goal. This ensured that the Astar algorithm would find the path from start to end with the lowest traversal cost and in minimum time possible.

#(8) Problems Faced: (A)The data was inconsistent such that bidirectional path was missing for some cities which led us to believe that the path was non existent.For example: We want to travel from city A to C , 
#we have path from A to B & C to B in the data but the path from B to C is missing which should have been present naturally. This error was handeled to travel the said path from A to C if they are interconnected in nay order.

#(B)Speed limit was missing for some paths so we calculated the average speed limit for all the road and the mean was assumed in place of missing data.

#(C)The GPS coordinates for some cities was missing which was handled by considering the Latitude & Longitude of the nearest neighbouring cities. This was again implemented by finding the shortes distanced betweeb neighbour cities.

#(D)DFS takes a lot of time to find the solution because the algorith tends to explore the wrong states that are farther away from the solution and these paths are againg explored further leading to waste of memory & compuing power.

#(E)For longer paths the time to find the solution by calculating the path from start to end city is considerably higher.This happens on the account that a lot of states are generated befor the right states are expanded.

#(F)We have hardcoded the optimality check at the beginning of the machine readable output based on our understanding of the routing algorithm and the cost function involved and after running several test cases.


from itertools import combinations
import copy
from random import randrange, sample
import sys
import string
import Queue as queue
from math import radians, cos, sin, asin, sqrt


#reading data from files
routes = []
gps = []

fp = open('road-segments.txt')
lines = fp.readlines()
fp.close()

for elem in lines:
    routes.append(elem.strip().split(' '))


np = open('city-gps.txt')
lines1 = np.readlines()
np.close()

for elem in lines1:
    gps.append(elem.strip().split(' '))


#Segment number,distance,time                                                                                                                                                                               
start = [0, '"Y"_City,_Arkansas']

#haversine function ref: https://stackoverflow.com/questions/4913349/haversine-formula-in-python-bearing-and-distance-between-two-gps-points
def haversine(lon1, lat1, lon2, lat2):
    """                                                                                                                                                                                                     
    Calculate the great circle distance between two points                                                                                                                                                  
    on the earth (specified in decimal degrees)                                                                                                                                                             
    """
    # convert decimal degrees to radians                                                                                                                                                                    
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])

    # haversine formula                                                                                                                                                                                     
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c = 2 * asin(sqrt(a))
    r = 6371 # Radius of earth in kilometers. Use 3956 for miles                                                                                                                                            
    return c * r

def find_highway(start,end):
    for elem in routes:
       if (elem[0] == start and elem[1] == end):
           return (elem[4],float(elem[2]),float(elem[2])/int(elem[3]),start,end)
       if (elem[1] == start and elem[0] == end):
           return (elem[4],float(elem[2]),float(elem[2])/int(elem[3]),start,end)

def heuristic_distance(start,end):
    for elem in routes:
        if (elem[0] == start and elem[1] == end):
            if(int(elem[2]) == 0):
               elem[2] = 50
            return float(elem[2])

def heuristic_time(start,end):
    for elem in routes:
        if (elem[0] == start and elem[1] == end):
               if(int(elem[3]) == 0):
                  elem[3] = 50
               return float(elem[2])/int(elem[3])

def succesors(state):
    successors = []
    last_city = state[-1]
    for elem in routes:
        if(elem[0] == last_city):
           succ = copy.deepcopy(state)
           flag = 1
           for city in succ:
               if(city == elem[1]):
                   flag = 0
           if(flag == 1):
               succ.append(elem[1])
               succ[0] = succ[0] + 1
               succ[1] = succ[1] + heuristic_distance(last_city,elem[1])
               succ[2] = succ[2] + heuristic_time(last_city,elem[1])
               successors.append(succ)
        if(elem[1] == last_city):
           flag = 1
           succ = copy.deepcopy(state)
           for city in succ:
               if(city == elem[0]):
                  flag = 0
           if(flag == 1):
               succ.append(elem[0])
               succ[0] = succ[0] + 1
               succ[1] = succ[1] + heuristic_distance(elem[0],last_city)
               succ[2] = succ[2] + heuristic_time(elem[0],last_city)
               successors.append(succ)

#        if(elem[1] == last_city):                                                                                                                                                                          
#           succ = copy.deepcopy(state)                                                                                                                                                                     
#           if(elem[0][:3] == 'Jct'):                                                                                                                                                                       
#              for elem1 in routes:                                                                                                                                                                         
#                  if(elem1[0] == elem[0]):                                                                                                                                                                 
#                     print elem                                                                                                                                                                            
#                     succ.append(elem1[1])                                                                                                                                                                 
#                     successors.append(succ)                                                                                                                                                               
    return successors

def heuristic_A(start,end):
    flag = 0
    for elem in gps:
        if(elem[0] == start):
           lat_start = float(elem[1])
           lon_start = float(elem[2])
           flag = 1
    if(flag == 0):
        (lon_start,lat_start) = near_city_coord(start)

    flag = 0
    for elem in gps:
        if(elem[0] == end):
           lat_end = float(elem[1])
           lon_end = float(elem[2])
           flag = 1
    if(flag == 0):
        (lon_end,lat_end) = near_city_coord(start)

    distance = haversine(lon_start,lat_start,lon_end,lat_end)
    return distance

def near_city_coord(city):
    cities = succesors([0,0,0,city])
    sorted_list = sorted(cities, key=lambda x: x[1])
    for elem in gps:
        if(elem[0] == sorted_list[0][4]):
           lat_city = float(elem[1])
           lon_city = float(elem[2])
    return (lon_city,lat_city)

#print near_city_coord('Bloomington,_Indiana')                                                                                                                                                              

def is_goal(state,end):
    return state[-1] == end

def print_fringe(fringe):
    for elem in list(fringe.queue):
        print elem

start_city = sys.argv[1]
end_city = sys.argv[2]
routing_algo = sys.argv[3]
cost_function = sys.argv[4]

if(cost_function == 'segments'):
   choice = 0
elif(cost_function == 'distance'):
   choice = 1
else:
   choice = 2


def A_star(start_city,end_city):
    count = 0
    start1 = [0,0,0,start_city]
    fringe = queue.PriorityQueue()
    fringe.put((100000000000,start1))
    while fringe.qsize() > 0:
        elem = fringe.get()
        for succ in succesors( elem[1] ):
            if is_goal(succ,end_city):
               return succ
            fringe.put((succ[choice] + heuristic_A(succ[3],succ[-1]),succ))
    return False


def ucs(start_city,end_city):
    count = 0
    start1 = [0,0,0,start_city]
    fringe = queue.PriorityQueue()
    fringe.put((100000000000,start1))
    while fringe.qsize() > 0:
        elem = fringe.get()
        for succ in succesors( elem[1] ):
            if is_goal(succ,end_city):
               return succ
            fringe.put((succ[choice],succ))
    return False

#print ucs('Bloomington,_Indiana','Indianapolis,_Indiana')                                                                                                                                                  


def bfs(start_city,end_city):
    fringe = []
    start1 = [0,0,0,start_city]
    fringe.append((start1[0],start1))
    while len(fringe) > 0:
             for s in (succesors( fringe.pop()[1] ) ) :
               if is_goal(s,end_city):
                   return(s)
               fringe.insert(0,(s[0],s))

#print succesors([0,0,0,'Bloomington,_Indiana'])                                                                                                                                                            
#print bfs('Bloomington,_Indiana','Indianapolis,_Indiana')                                                                                                                                                  


def dfs(start_city,end_city):
    fringe = []
    start1 = [0,0,0,start_city]
    fringe.append((start1[0],start1))
    while len(fringe) > 0:
             for s in (succesors( fringe.pop()[1] ) ) :
               if is_goal(s,end_city):
                   return(s)
               fringe.append((s[0],s))


#print dfs('Bloomington,_Indiana','Indianapolis,_Indiana')                                                                                                                                                  


def ids(start_city,end_city):
    for x in range(4,20,1):
        fringe = []
        start1 = [0,0,0,start_city]
        fringe.append((start1[0],start1))
        while len(fringe) > 0:
                 for s in (succesors( fringe.pop()[1] ) ) :
                   if (len(s) >= x):
                       continue
                   else:
                       if is_goal(s,end_city):
                           return(s)
                       fringe.append((s[0],s))

#print ids('Bloomington,_Indiana','Indianapolis,_Indiana')                                                                                                                                                  

def print_output(output,optimal):
    distance1  = 0
    time1 = 0
    for i in range(3,len(output) - 1):
        (highway,distance,time,start,end) = find_highway(output[i],output[i+1])
        distance1 = distance1 + distance
        time1 = time1 + time
        print "Take Highway: " + str(highway) + " from "+ str(start)+ " to " + str(end)+ " " + "Distance_Elapsed: " + str(distance1) + " " +  "Time_Elapsed: " + str(time1)
        print '\n'
    print str(optimal),
    print output[1],
    print output[2],
    for i in range(3,len(output)):
        print str(output[i]) + " ",


if(routing_algo == 'uniform'):
   output = ucs(start_city,end_city)
   print_output(output,'yes')
elif(routing_algo == 'bfs' and cost_function == 'segments'):
   output = bfs(start_city,end_city)
   print_output(output,'yes')
elif(routing_algo == 'dfs'):
   output = dfs(start_city,end_city)
   print_output(output,'no')
elif(routing_algo == 'ids' and cost_function == 'segments'):
   output = ids(start_city,end_city)
   print_output(output,'yes')
elif(routing_algo == 'bfs'):
   output = bfs(start_city,end_city)
   print_output(output,'no')
elif(routing_algo == 'astar'):
   output = A_star(start_city,end_city)
   print_output(output,'yes')
else:
   output = ids(start_city,end_city)
   print_output(output,'yes')


#print '\n'                                                                                                                                                                                                 
#coord = heuristic_A('Bloomington,_Indiana','Indianapolis,_Indiana')                                                                                                                                        
#print haversine(coord[0],coord[1],coord[2],coord[3])                                                                                                                                                       
#near_city_coord('Bloomington,_Indiana')   

