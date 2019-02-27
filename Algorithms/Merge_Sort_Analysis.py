import time
import matplotlib.pyplot as plt

#Merge Sort
#1.Dividing array into two parts until only element left
#2.Then recursively placing them in ascending order
#Reference : https://www.pythoncentral.io/merge-sort-implementation-guide/

def merge(left,right):
    
    f = []
    while len(left) != 0 and len(right) != 0:
        if left[0] < right[0]:
            f.append(left[0])
            left.remove(left[0])
        else:
            f.append(right[0])
            right.remove(right[0])
    if len(left) == 0:
        f = f + right
    else:
        f = f + left
    return f

def mergeSort(mlist):
    
    if len(mlist) == 0 or len(mlist) == 1:
        return mlist
    else:
        mid = len(mlist)//2
        left = mergeSort(mlist[:mid])
        right = mergeSort(mlist[mid:])
        return merge(left,right)



#Largest Element by Median of Medians
#Reference : https://brilliant.org/wiki/median-finding-algorithm/

def largest_elem(arr,nth):
    medians = []
    left = []
    right = []
    div_list = [arr[i:i+5] for i in range(0, len(arr), 5)]
    for elem in div_list:
        sorted(elem)
        medians.append(elem[len(elem)//2])

    if len(medians) <= 5:
        sorted(medians)
        pivot = medians[len(medians)//2]
    else:
        pivot = largest_elem(medians, len(medians)//2)


    for elem in arr:
        if(elem < pivot):
           left.append(elem)
        else:
           right.append(elem)

    if nth < len(left):
       return median_of_medians(left,nth)
    elif nth > len(right):
       return median_of_medians(right,nth-len(left)-1)
    else:
       return pivot



fp = open('/Users/tejasdeoras/Downloads/input-3.txt')
lines = fp.readlines()
fp.close()
results = list(map(int, lines))
print(results)


#Largest Element By Merge Sort

def largest_elem_merge(A,nth):
    mergesort(A)
    return A[nth+1]


#Running Largest Element by Merge Sort for max input size 10000
#Running at 500 input intervals for 3 times and averaging them

fresult = []
inputsize = []
for i in range(500, 10500, 500):
    avg = 0
    inputsize.append(i)
    for j in range(0, 3, 1):
        start = time.time()
        largest_elem_merge(results[0:i],3)
        end = time.time()
        elapsed = end - start
        avg = avg + elapsed

    fresult.append(avg/3)
    
print(fresult)
print(len(fresult))
print(inputsize)
print(len(inputsize))


#Running Largest Element by Median of Medians for max input size 10000
#Running at 500 input intervals for 3 times and averaging them

fresult1 = []
inputsize1 = []
for i in range(500, 10500, 500):
    avg = 0
    inputsize1.append(i)
    for j in range(0, 3, 1):
        start = time.time()
        largest_elem(results[0:i],3)
        end = time.time()
        elapsed = end - start
        avg = avg + elapsed

    fresult1.append(avg/3)
    
print(fresult1)
print(len(fresult1))
print(inputsize1)
print(len(inputsize1))


#Plotting both the largest element algorithm

plt.ylabel('Time(seconds)')
plt.xlabel('Input Size')
plt.plot(inputsize, fresult)
plt.plot(inputsize, fresult1)
plt.show()




