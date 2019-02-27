import re
from collections import Counter
import heapq
import copy

words = []
char_set1 = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z",".","?","!",",","'"," "]


#Read Text File
with open('book.txt') as f:
  while True:
    c = f.read(1)
    if c in char_set1:
       words.append(c)
    if not c:
      break

#Counter for Frequencies
cnt = Counter(words)
freq = cnt.most_common()
                                                                                                                                                                                             

class Node(object):
    def __init__(self, data):
        self.data = data
        self.freq = 0
        self.right = -1
        self.left = -1

#Node for Tree
Nodes = []
for elem in freq:
    my_node = Node(elem[0])
    my_node.freq = elem[1]
    Nodes.append((my_node.freq,my_node))


Nodes1 = copy.deepcopy(Nodes)


Q = []
for elem in Nodes:
    heapq.heappush(Q, elem)

#Huffman Encoding using heaps
for i in range(0,len(Q)-1):
    elem1 = heapq.heappop(Q)
    elem2 = heapq.heappop(Q)
    newfreq = elem1[1].freq + elem2[1].freq
    my_new_node = Node(elem1[1].data+elem2[1].data)
    my_new_node.freq = newfreq
    my_new_node.left = elem1[1]
    my_new_node.right = elem2[1]
    heapq.heappush(Q, (my_new_node.freq,my_new_node))

root = Q[0][1]
huff = []

#Tree traversal
def traverseTree(node,bit):
    if node.left == -1 and node.right == -1:
       print node.data,bit
       huff.append((node.data,node.freq,bit,len(bit),node.freq*len(bit)))
    else:
       traverseTree(node.left, bit + '0')
       traverseTree(node.right, bit + '1')

print 'Huffman Encoding'
traverseTree(root, '')
print '\n'

Q1 = []

char_set = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z",".","?","!",",","'"," "]
                                                                                                                                                                                        

char_set1 = []
for elem in freq:
    char_set1.append(elem[0])

for elem in char_set:
    if elem not in char_set1:
       my_node = Node(elem)
       my_node.freq = 0
       Nodes1.append((my_node.freq,my_node))

for elem in Nodes1:
    Q1.append(elem)

#Fixed Length Encoding
while len(Q1) > 1:
      elem1 = Q1.pop()
      elem2 = Q1.pop()
      newfreq = elem1[1].freq + elem2[1].freq
      my_new_node = Node(elem1[1].data+elem2[1].data)
      my_new_node.freq = newfreq
      my_new_node.left = elem1[1]
      my_new_node.right = elem2[1]
      Q1.insert(0,(my_new_node.freq,my_new_node))

root1 = Q1.pop()[1]

print 'Fixed Length Encoding'
traverseTree(root1, '')


#Calculating Discussion Calculations(Bits Used)
tot1 = 0
for elem in huff:
#    print elem                                                                                                                                                                                             
    tot1 = tot1 + elem[4]

#print tot1          