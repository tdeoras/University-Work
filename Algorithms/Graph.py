#Reference : https://www.geeksforgeeks.org/check-if-a-given-graph-is-bipartite-using-dfs/
#Reference : Some code is also done with classmates help
#Graph creating Adjacecy List



#filename = 'bipartite.txt'
#edges = []
#f=open(filename,'r')
#for i, line in enumerate(f):
#    if i == 0:
#       n = line
#    else:
#       line = line.split()
#       edges.append(line[0])



#edges1 = []
#for elem in edges:
#    edges1.append((int(elem[1]),int(elem[3])))




#V = []
#for elem in edges1:
#    V.append(elem[0])
#    V.append(elem[1])

#V = list(set(V))



#AdjancecyList = {}

#for elem in V:
#    AdjancecyList[elem] = []


#for elem in AdjancecyList:
#    for elem1 in edges1:
#        if elem1[0] == elem:
#           n1 = elem1[1]
#           AdjancecyList[elem].append(n1)
#        if elem1[1] == elem:
#           n1 = elem1[0]
#           AdjancecyList[elem].append(n1)







def read_input(file):

	adjacencylist={}
	val1 = 1

	with open(file,"r") as f :
		for line in f:
			if len(line) > 2:
				if len(adjacencylist) == 2:
					val1 = adjacencylist.keys()[0]
				if line[1] not in adjacencylist:
					adjacencylist[line[1]] = [line[3]]
				else : 
					adjacencylist[line[1]].append(line[3])
				if line[3] not in adjacencylist:
						adjacencylist[line[3]] = [line[1]]
				else :
					adjacencylist[line[3]].append(line[1])
	return adjacencylist,val1


class Vertices:
    def __init__(self,val):
        self.val = val
        self.color = 'white'



# Checking Biparate
def Bipartite(adjacencylist,val1):
	Colors = {}
	visitednodes={}
	for node in adjacencylist.keys():
		Colors[node] = "white"
		visitednodes[node] = False
	Colors[val1] = "red" 
	queue =[val1]
	while len(queue)>0:
		u= queue.pop()
		for x in adjacencylist[u]:
			if u in x:
				return False
		if not visitednodes[u]:
			visitednodes[u] = True
			for x in adjacencylist[u]:
				queue.insert(0,x)
				if Colors[u] != 'white' and Colors[u] == Colors[x]:
					return False
				if Colors[x] == 'white' :
					if Colors[u] == 'red':
						Colors[x] = 'blue'
					else:
						Colors[x] = 'red'
	blue = []
	red = []
	for x in Colors:
		if Colors[x] == "blue":
			blue.append(x)
		else:
			red.append(x)
	print "Blue" , blue
	print "Red" , red
	return True




f = "bipartite.txt"
adjacencylist,val1=read_input(f)
print "Bipartite : " + str(Bipartite(adjacencylist,val1))