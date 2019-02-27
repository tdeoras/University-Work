#!/usr/bin/python
#
# ./ocr.py : Perform optical character recognition, usage:
#     ./ocr.py train-image-file.png train-text.txt test-image-file.png
# 
# Tejas Deoras : tdeoras  
# Animesh Sagar : asagar
# Shashank Mittal : shasmitt
#
#I. Simplified Algorithm:
#   1.A sum was taken comparing pixel to pixel.
#   2.The letter with the highest sum was taken.
#
#II. HMM:
#.   1. Emission probibilty was calculated using comparing pixel by pixel and multiplying 0.6 for match and 0.4 for no match(40% noise) 
#.   2. The transiitional probilties were calculated from the training in part1
#    3.A veterbi matrix was constructed with row indicating the type of label and columns indicating words in sentence.
#.   4.The concept was refered from https://www.youtube.com/watch?v=_568XqOByTs&t=572s
#
#Problems Faced:
# 1. Missing transitional probabilities: The missing probabilities were handled by returning a small probabilty of 
#    0.0000001
#
# 2. Veterbi proabilities reaching 0: For long sentences the probabilities reached so low that they reached 0 causing the program to predict
#    wrong ltters at the end of senetence.This was solved by using log values of the probabilities instead. 
#
# 3. Noisy images : Noise caused the emission probabilities to go out of balance hence resulting in false letter predictions.
#
# 4. UPPER CASE examples : When all letters in a sentence were uppercase the simple performed better than HMM. This was due to lack of 
#    upper case senetences in the training data causing the transitional probabilities to go out of balance.             
#
#
import random
import math
from collections import Counter
import numpy as np
from PIL import Image, ImageDraw, ImageFont
import sys
import math

CHARACTER_WIDTH=14
CHARACTER_HEIGHT=25


def load_letters(fname):
    im = Image.open(fname)
    px = im.load()
    (x_size, y_size) = im.size
#    print im.size
#    print int(x_size / CHARACTER_WIDTH) * CHARACTER_WIDTH
    result = []
    for x_beg in range(0, int(x_size / CHARACTER_WIDTH) * CHARACTER_WIDTH, CHARACTER_WIDTH):
        result += [ [ "".join([ '*' if px[x, y] < 1 else ' ' for x in range(x_beg, x_beg+CHARACTER_WIDTH) ]) for y in range(0, CHARACTER_HEIGHT) ], ]
    return result

def load_training_letters(fname):
    TRAIN_LETTERS="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789(),.-!?\"' "
    letter_images = load_letters(fname)
    return { TRAIN_LETTERS[i]: letter_images[i] for i in range(0, len(TRAIN_LETTERS) ) }





#####
# main program
(train_img_fname, train_txt_fname, test_img_fname) = sys.argv[1:]
train_letters = load_training_letters(train_img_fname)
test_letters = load_letters(test_img_fname)

#TRAIN_LETTERS="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789(),.-!?\"' "
#for elem in TRAIN_LETTERS:
#    print len(train_letters[elem])
#    break
#print len(test_letters[2]

def initialize_transitional():
    trans = []
    trans1 = []
    letters = []
    end = []
    initial = []
    count_line = 0
    exemplars = []
    file = open(train_txt_fname, 'r');
    for line in file:
        line.strip("ADJ").strip("ADV").strip("ADP").strip("CONJ").strip("DET").strip("NOUN").strip("NUM").strip("PRON").strip("PRT").strip("VERB")
        for i in range(0,len(line)-1):
            trans.append((line[i],line[i+1]))
            trans1.append(line[i])
        trans1.append(line[-1])
        trans.append(('start',line[0]))
        trans.append(('end',line[-1]))
        count_line = count_line + 1        
    
    return Counter(trans),Counter(trans1),count_line
   
trans,trans1,count_line = initialize_transitional()
count_line = count_line * 1.0
initialize_transitional()
#print trans
#print trans1

def find_emission(pos,pos1):
    match = 1
    for i in range(25):
        for j in range(14):
            if test_letters[pos][i][j] == train_letters[pos1][i][j]:
               match = match * 0.67
            else:
               match = match * 0.33
    e = match * 1.0
    r = match/350.0
    per = r * 100.0
    if per > 80:
       val = 1
    else:
       val = 0
#    return match * 100000000000000000000000000000000000.0
    return math.log(match)     

def find_trans(pos,pos1):
    if trans[(pos,pos1)] != 0 and trans1[pos] != 0 and pos != 'start' and pos != 'end':
       trans[(pos,pos1)] = trans[(pos,pos1)] * 1.0
       trans1[pos] = trans1[pos] * 1.0
       return math.log((trans[(pos,pos1)]/trans1[pos]) * 1.0)
    elif pos == 'start' and trans[(pos,pos1)] != 0:
       trans[(pos,pos1)] = trans[(pos,pos1)] * 1.0
       return math.log((trans[(pos,pos1)]/count_line) *  1.0)
    elif pos == 'end' and trans[(pos,pos1)] != 0:
       trans[(pos,pos1)] = trans[(pos,pos1)] * 1.0
       return math.log((trans[(pos,pos1)]/count_line) * 1.0)
    else:
       return math.log(0.000001)

   
def letter_match(letter):
    current_max = 0
    TRAIN_LETTERS="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789(),.-!?\"' "
    for elem in TRAIN_LETTERS:
        match = 0
        for i in range(25):
            for j in range(14):
                if train_letters[elem][i][j] == letter[i][j]:
                   match = match + 1

        if current_max < match:
           current_max = match
           current_alpha = elem
    return current_alpha

def simple(test):
    result = ''
    for elem in test:
        result = result + letter_match(elem)
    return result

test12 = simple(test_letters)
print 'Simple: ' + test12

#print 'Hello'
#print find_emission(32,'S')
#print find_trans('C','O')

def hmm_viterbi(sentence,bal):
        types = []
        TRAIN_LETTERS="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789(),.-!?\"' "
        for elem in TRAIN_LETTERS:
            types.append(elem)
        viterbi_matrix  = [[None for x in range(len(types))] for y in range(len(sentence)+1)]
        for i in range(len(sentence) + 1):
            if i == 0:
               for j in range(0,len(types)):
#                   print find_emission(i,types[j]),sentence[i],types[j]
#                   print find_trans('start',types[j]),'start',types[j]
                   viterbi_matrix[i][j] = (find_emission(i+bal,types[j]) + find_trans('start',types[j]),'start')
            elif i == len(sentence):
                 for j in range(0,len(types)):
                   pos1 = []
                   for k in range(0,len(types)):
                       pos1.append(find_emission(i-1+bal,types[j]) + viterbi_matrix[i-1][k][0] + find_trans('end',types[j]))
#                       print find_emission(i-1,types[j]),sentence[i-1],types[j]
#                       print viterbi_matrix[i-1][k]
#                       print find_trans('end',types[j]),'end',types[j]
                   max_prob = max(pos1)
                   viterbi_matrix[i][j] = (max_prob,types[pos1.index(max_prob)])
            else:
               for j in range(0,len(types)):
                   pos1 = []
                   for k in range(0,len(types)):
                       pos1.append(find_emission(i+bal,types[j]) + viterbi_matrix[i-1][k][0] + find_trans(types[k],types[j]))
#                       print find_emission(i,types[j]),sentence[i],types[j]
#                       print viterbi_matrix[i-1][k]
#                       print types[k]
#                       print find_trans(sentence[i-1],types[j]),types[k],types[j]
                   max_prob = max(pos1)
                   viterbi_matrix[i][j] = (max_prob,types[pos1.index(max_prob)])
        
        result = []        
        for i in range(0,len(sentence)+1):
            pos2 = []
            for j in range(0,len(types)):
                pos2.append(viterbi_matrix[i][j][0])
            result.append(viterbi_matrix[i][pos2.index(max(pos2))][1])
#            print 'Came from'
#            print types[pos2.index(max(pos2))]                
                
#        print result[1:]
            
         
#        print viterbi_matrix
        return result[1:]

str2 = ''
s = len(test_letters)
for i in range(s):
    str2 = str2 + 'a'

answer = hmm_viterbi(str2,0)
str3 = ''
for i in range(len(answer)):
    str3 = str3 + answer[i]
print 'HMM: ' + str3
print 'Final Answer:'
print str3

## Below is just some sample code to show you how the functions above work. 
# You can delete them and put your own code here!


# Each training letter is now stored as a list of characters, where black
#  dots are represented by *'s and white dots are spaces. For example,
#  here's what "a" looks like:
#print "\n".join([ r for r in train_letters['a'] ])

# Same with test letters. Here's what the third letter of the test data
#  looks like:
#print "\n".join([ r for r in test_letters[2] ])



