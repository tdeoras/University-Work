import time
import matplotlib.pyplot as plt

#Referred from :- http://interactivepython.org/runestone/static/pythonds/SortSearch/TheBubbleSort.html
def bubblesort(listsort):
    length = len(listsort)
    flag = 0;
    flagno = length -1

    while flag == 0 and flagno > 0:
        flag = 1
        for i in range(length-2):
            if listsort[i] > listsort[i+1]:
                flag = 0
                temp = listsort[i]
                listsort[i] = listsort[i+1]
                listsort[i+1] = temp

        flagno = flagno - 1

#Reading the inputs from text file
fp = open('/Users/tejasdeoras/Downloads/input.txt')
lines = fp.readlines()
fp.close()
results = list(map(int, lines))

#Running the inputs at values of 50,100,..1000 3 times each and calculating average runtime
fresult = []
inputsize = []
for i in range(50, 1050, 50):
    avg = 0
    inputsize.append(i)
    for j in range(0, 3, 1):
        start = time.time()
        bubblesort(results[0:i])
        end = time.time()
        elapsed = end - start
        avg = avg + elapsed

    fresult.append(avg/3)

#using matplot to plot the graph
print(fresult)
print(len(fresult))
print(inputsize)
print(len(inputsize))
plt.ylabel('Time(seconds)')
plt.xlabel('Input Size')
plt.plot(inputsize, fresult)
plt.show()