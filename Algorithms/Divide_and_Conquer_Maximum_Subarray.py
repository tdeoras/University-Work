import time
import matplotlib.pyplot as plt


#Reading input from Input File 
fp = open('/Users/tejasdeoras/Downloads/input-2.txt')
lines = fp.readlines()
fp.close()
results = list(map(int, lines))


#Brute Force Algorithm
#Refered from : https://stackoverflow.com/questions/41904746/why-is-the-maximum-sum-subarray-brute-force-on2

def max_subarray(array):
      maximum = float('-inf')
      for i in range(0, len(array)):
            current = 0
            for j in range(i, len(array)):
                current += array[j]
                temp = maximum
                maximum = max(current, maximum)
                if(temp != maximum):
                    low = i
                    top = j
      

#Recurssion Function to divide the array
#1.Check Sum on Left
#2.Check Sum on Right
#3.Check Cross Sum
#4.Return whichever is maximum
#Refered from: https://www.sanfoundry.com/python-program-solve-maximum-subarray-problem-using-divide-conquer/

def max_subarray_divide(array,start,end):
    if start == end - 1:
        return start,end,array[start]
    
    mid = (start + end)//2
    left_start,left_end,left_max = max_subarray_divide(array,start,mid)
    right_start,right_end,right_max = max_subarray_divide(array,mid,end)
    cross_start,cross_end,cross_max = max_crossing(array,start,mid,end)
    
    if(max(left_max,right_max,cross_max) == left_max):
        return left_start,left_end,left_max
    elif(max(left_max,right_max,cross_max) == right_max):
        return right_start,right_end,right_max
    else:
        return cross_start,cross_end,cross_max
     
#Function from Calculating Sums
  
def max_crossing(array,start,mid,end):
    left_sum = float('-inf')
    current = 0
    cross_start = mid
    for i in range(mid-1,start-1,-1):
        current = current + array[i]
        temp = left_sum
        left_sum = max(current,left_sum)
        if(temp != left_sum):
            cross_start = i
    
    
    right_sum = float('-inf')
    current = 0
    cross_end = mid + 1
    
    for j in range(mid,end):
        current = current + array[j]
        temp = right_sum
        right_sum = max(current,right_sum)
        if(temp != right_sum):
            cross_end = j+1
    
    cross_sum = right_sum + left_sum
    
    return cross_start,cross_end,cross_sum


#Running Brute force for max input size 10000
#Running at 500 input intervals for 3 times and averaging them

fresult = []
inputsize = []
for i in range(500, 10500, 500):
    avg = 0
    inputsize.append(i)
    for j in range(0, 3, 1):
        start = time.time()
        max_subarray(results[0:i])
        end = time.time()
        elapsed = end - start
        avg = avg + elapsed

    fresult.append(avg/3)
    
print(fresult)
print(len(fresult))
print(inputsize)
print(len(inputsize))


#Running Divide and Conquer for max input size 10000
#Running at 500 input intervals for 3 times and averaging them

fresult1 = []
inputsize1 = []
for i in range(50, 10500, 500):
    avg = 0
    inputsize1.append(i)
    for j in range(0, 3, 1):
        start = time.time()
        max_subarray_divide(results[0:i],0,len(results[0:i]))
        end = time.time()
        elapsed = end - start
        avg = avg + elapsed

    fresult1.append(avg/3)
    
print(fresult1)
print(len(fresult1))
print(inputsize1)
print(len(inputsize1))


#Plotting results of Both Brute Force and Divide and Conquer on Graph

plt.ylabel('Time(seconds)')
plt.xlabel('Input Size')
plt.plot(inputsize, fresult)
plt.plot(inputsize, fresult1)
plt.show()








