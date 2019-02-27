#!/usr/bin/env python2 

# Design decisions
# Stop Words : Stop words have been ignored as they only provide structure to the sentence and do not relate directly to Location
# Balance the Probabilities : A 0.1 has been added to avoid probabilities reaching 0 when a word has no occurences
# Counter Library : Counter has been used to create dictionary
# Vectorizing Tweets : Tweets have been vectorized with tweets in the form of words in a list
# Processing Words : Words have been changed to lowercase for avoiding Capital and Lowercase same words being distinct    


                                                                                                                                                                                     
from itertools import combinations
import copy
from random import randrange, sample
import sys
import string
import Queue as queue
import sys
import time
import re
from collections import Counter
from operator import itemgetter

file1 = sys.argv[1]
file2 = sys.argv[2]
file3 = sys.argv[3]


stop_words = ['all', 'whys', 'being', 'over', 'isnt', 'through', 'yourselves', 'hell', 'its', 'before', 'wed', 'with', 'had', 'should', 'to', 'lets', 'under', 'ours', 'has', 'ought', 'do', 'them', 'his',\
 'very', 'cannot', 'they', 'werent', 'not', 'during', 'yourself', 'him', 'nor', 'wont', 'did', 'theyre', 'this', 'she', 'each', 'havent', 'where', 'shed', 'because', 'doing', 'theirs', 'some', 'whens', '\
up', 'are', 'further', 'ourselves', 'out', 'what', 'for', 'heres', 'while', 'does', 'above', 'between', 'youll', 'be', 'we', 'who', 'were', 'here', 'hers', 'by', 'both', 'about', 'would', 'wouldnt', 'did\
nt', 'ill', 'against', 'arent', 'youve', 'theres', 'or', 'thats', 'weve', 'own', 'whats', 'dont', 'into', 'youd', 'whom', 'down', 'doesnt', 'theyd', 'couldnt', 'your', 'from', 'her', 'hes', 'there', 'onl\
y', 'been', 'whos', 'hed', 'few', 'too', 'themselves', 'was', 'until', 'more', 'himself', 'on', 'but', 'you', 'hadnt', 'shant', 'mustnt', 'herself', 'than', 'those', 'he', 'me', 'myself', 'theyve', 'thes\
e', 'cant', 'below', 'of', 'my', 'could', 'shes', 'and', 'ive', 'then', 'wasnt', 'is', 'am', 'it', 'an', 'as', 'itself', 'im', 'at', 'have', 'in', 'id', 'if', 'again', 'hasnt', 'theyll', 'no', 'that', 'w\
hen', 'same', 'any', 'how', 'other', 'which', 'shell', 'shouldnt', 'our', 'after', 'most', 'such', 'why', 'wheres', 'a', 'hows', 'off', 'i', 'youre', 'well', 'yours', 'their', 'so', 'the', 'having', 'onc\
e','','i','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',' ']

#def clean_text(text):                                                                                                                                                                                      
#     only_chars = '[^a-zA-Z\s]+'                                                                                                                                                                           
#     text = re.sub(only_chars, '', text)                                                                                                                                                                   
#     text = re.sub(' +', ' ', text)                                                                                                                                                                        
#     text = text.replace('\r', '')                                                                                                                                                                         
#     text = text.replace('\n', '')                                                                                                                                                                         
#     return text.strip().lower()                                                                                                                                                                           


def getWords(text):
     list2 = []
     list1 = re.compile('\w+').findall(text)
     for elem in list1:
         if elem.lower() not in stop_words:
            list2.append(elem.lower())
     return list2


TweetList = []
with open(file1,'r') as f:
            for line in f:
                TweetList.append(line.split(None, 1))

TweetListTest = []
with open(file2,'r') as f:
            for line in f:
                TweetListTest.append(line.split(None, 1))


TweetListProcessed = []

cities = []
for elem in TweetList:
    if len(elem) == 2 and elem[0] and re.search('[a-zA-Z]', elem[0]) and elem[0][0].isalpha():
       cities.append(elem[0])
       TweetListProcessed.append([elem[0],getWords(elem[1])])


TweetListTestProcessed = []

for elem in TweetListTest:
    if len(elem) == 2 and elem[0] and re.search('[a-zA-Z]', elem[0]) and elem[0][0].isalpha():
       TweetListTestProcessed.append(['est',elem[0],getWords(elem[1])])



#print len(cities)                                                                                                                                                                                          


def max_val(l, i):
    return max(enumerate(map(itemgetter(i), l)),key=itemgetter(1))

Probability_Cities = []
processed_cities = []

for elem in cities:
    if re.search(',_', elem):
       processed_cities.append(elem)

#print processed_cities                                                                                                                                                                                     

cityset = set(processed_cities)
city_unique = list(cityset)

#print city_unique                                                                                                                                                                                          


no_of_cities = float(len(processed_cities))

#print no_of_cities                                                                                                                                                                                         
#print city_unique                               
                                                                                                                                                                                        

for elem in city_unique:
    count = 0.0
    for elem1 in processed_cities:
        if elem == elem1:
           count = count + 1.0

    prob = float(count/no_of_cities)
#    print prob                                                                                                                                                                                             
    Probability_Cities.append([elem,prob])


#print Probability_Cities                                                                                                                                                                                   


def getWords(text):
     list2 = []
     list1 = re.compile('\w+').findall(text)
     for elem in list1:
#         print elem                                                                                                                                                                                        
         list2.append(elem.lower())
     return list2



#print TweetListProcessed                                                                                                                                                                                   
#print TweetListTestProcessed                                                                                                                                                                               

Word_City = []


for elem in Probability_Cities:
    Word_count = []
    for elem1 in TweetListProcessed:
        if elem[0].lower() == elem1[0].lower():
           for elem2 in elem1[1]:
               Word_count.append(elem2)
    Word_City.append([elem,Counter(Word_count)])


#for elem in Word_City:                                                                                                                                                                                     
#    print elem[0][0]                                                                                                                                                                                       

#print Word_City[0]                                                                                                                                                                                         
#print Probability_Cities                                                                                                                                                                                   

for elem1 in TweetListTestProcessed:
    list_prob = []
    for elem2 in Word_City:
        cnt = elem2[1]
        n = len(cnt)
        p = 1.0
        for elem3 in elem1[2]:
            s = cnt[elem3]
            p = p * float(float(s+0.1)/float(n))
#            print s,n                                                                                                                                                                                      
        p = p * elem2[0][1]
        list_prob.append([elem2[0][0],p])

#    print list_prob                                                                                                                                                                                        
    index = max_val(list_prob, -1)
    result1 = list_prob[index[0]]
    city_prediction = result1[0]
    elem1[0] = city_prediction


count = 0.0
for elem in TweetListTestProcessed:
    if elem[0] == elem[1]:
       count = count + 1.0

print 'Accuracy is: ',
print float(float(count)/float(len(TweetListTestProcessed)))*100
print '\n'

f = open(file3,"w+")
for elem in TweetListTestProcessed:
    str1 = ''
    for elem1 in elem[2]:
        str1 = str1 + elem1 + ' '
    f.write('%r %r %r\n' % (elem[0],elem[1],str1))


for elem in Word_City:
    if re.search(',_', elem[0][0]):
       print elem[0][0]
       cnt = elem[1]
       count = 0
       print cnt.most_common(5)
    print '\n'




