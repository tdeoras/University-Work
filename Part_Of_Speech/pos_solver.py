###################################
# CS B551 Fall 2018, Assignment #3
#
# Tejas Deoras : tdeoras  
# Animesh Sagar : asagar
# Shashank Mittal : shasmitt
# 
####
# I. Simplified Algorithm :
#    1.The emission probabilty of each word with the types of label was calculated
#    2.The label with highest probabilty was selected
# II. HMM_veterbi :   
#    1.The emmision, inital and transitional probabilites were calculated
#    2.A veterbi matrix was constructed with row indicating the type of label and columns indicating words in sentence.
#.   3.The concept was refered from https://www.youtube.com/watch?v=_568XqOByTs&t=572s
# III. Complex_MCMC:
#    1.The emission and two types of transitional probabilties were calculated according to bayes net
#    2.Gibs sampling was used to generate samples
#.   3.The highest occuring tag in the sample was selected for that particular word 
#
# Problems Faced:
# 1. Missing emission and transitional probabilities: The missing probabilities were handled by returning a small probabilty of 
#    0.00000000000000000000000000000000000000001
#
# 2. Veterbi proabilities reaching 0: For long sentences the probabilities reached so low that they reached 0 causing the program to predict
#    wrong tags at the end of senetence.This was solved by using log values of the probabilities instead.
#
# 3. MCMC taking large no of samples for getting accurate results: The MCMC required a sample size of 1000 for getting reasonobale accuracy.This was solved by
#    taking the stating partile of Gibs sampling the result of simplified rather that generating it randomly.
#
# 4. Probailties not adding to 1 for np.random : np.random requires all proabilities of each of the tag to sum to 1. This was balancing the probilities 
#    to sum up to 1.
# 
####

import random
import math
from collections import Counter
import numpy as np
import math

# We've set up a suggested code structure, but feel free to change it. Just
# make sure your code still works with the label.py and pos_scorer.py code
# that we've supplied.
#
class Solver:
    # Calculate the log of the posterior probability of a given sentence
    #  with a given part-of-speech labeling. Right now just returns -999 -- fix this!
    tr = Counter()
    tr1 = Counter()
    tr2 = Counter()
    tr3 = Counter()
    tr4 = Counter()
    tr5 = Counter()
    tr6 = Counter()
    tr7 = Counter()
    emission_prob = []
    transitional_prob = []
    initial_prob = []
    simple_result = []
    simple_posterior = 0
    veterbi_posterior = 0

    def find_emission(self,word,pos):
        for elem in Solver.emission_prob:
            if (word,pos) == elem[0]:
                if elem[1] != 0:
                   return math.log(elem[1])
        return math.log(0.00000000000000000000000000000000000000001)

    def find_trans(self,pos,pos1):
        for elem in Solver.transitional_prob:
            if(pos,pos1) == elem[0]:
                return math.log(elem[1])
        return math.log(0.00000000000000000000000000000000000000001)

    def find_emission1(self,word,pos):
        for elem in Solver.emission_prob:
            if (word,pos) == elem[0]:
                if elem[1] != 0:
                   return elem[1]
        return 0.00000000000000000000000000000000000000001
    
    def find_trans1(self,pos,pos1):
        for elem in Solver.transitional_prob:
            if(pos,pos1) == elem[0]:
                return elem[1]
        return 0.00000000000000000000000000000000000000001

    def posterior(self, model, sentence, label):
        if model == "Simple":
            result = 0
            for i in range(0,len(sentence)):
                result = result + self.find_emission(sentence[i],label[i])
            return result
                
        elif model == "Complex":

            result = 0
            for i in range(0,len(sentence)):
                if i == 0:
                   result = result + self.find_emission(sentence[i],label[i])
                elif i == 1:
                   result = result + self.find_emission(sentence[i],label[i]) + self.find_trans(label[i-1],label[i])
                else:
                   to1 = Solver.tr7[(label[i-2],label[i-1],label[i])] * 1.0
                   to2 = Solver.tr1[label[i]] * 1.0
                   to3 = to1/to2
                   if to3 == 0:
                      to3 = 0.00000000000000000000000000000000000000001
                   result = result + self.find_emission(sentence[i],label[i]) + self.find_trans(label[i-1],label[i]) + math.log(to3)
            return result

        elif model == "HMM":
            
            result = 0
            for i in range(0,len(sentence)):
                if i == 0:
                   result = result + self.find_emission(sentence[i],label[i])
                else:
                   result = result + self.find_emission(sentence[i],label[i]) + self.find_trans(label[i-1],label[i])
            return result

        else:
            print("Unknown algo!")

    # Do the training!
    #
    def train(self, data):
        for elem in data:
            Solver.tr3[elem[1][0]] += 1
            if len(elem[1]) > 2:
               Solver.tr4[elem[1][1]] += 1
            Solver.tr5[elem[1][-1]] += 1
            for i in range(0,len(elem[1])):
               Solver.tr[(elem[0][i],elem[1][i])] += 1
               Solver.tr1[(elem[1][i])] += 1
        for elem in data:
            for i in range(0,len(elem[1])-1):
                Solver.tr2[(elem[1][i],elem[1][i+1])] += 1
            for i in range(0,len(elem[1]) - 2):
                Solver.tr6[(elem[1][i],elem[1][i+2])] += 1
            for i in range(0,len(elem[1]) - 3):
                Solver.tr7[(elem[1][i],elem[1][i+2],elem[1][i+3])] += 1
        for elem in Solver.tr2:
            Solver.transitional_prob.append((elem,Solver.tr2[elem]/(Solver.tr1[elem[0]] * 1.0)))
        types = ['noun','verb','adp','.','det','adj','adv','pron','conj','prt','num','x']
        for elem in types:
            Solver.initial_prob.append((elem,(Solver.tr3[elem]/(len(data) * 1.0)))) 
        for elem in Solver.tr4:
            Solver.transitional_prob.append((('start',elem),Solver.tr4[elem]/(len(data) * 1.0)))
        for elem in Solver.tr5:
            Solver.transitional_prob.append((('end',elem),Solver.tr5[elem]/(len(data) * 1.0)))
        
    # Functions for each algorithm. Right now this just returns nouns -- fix this!
    #
    def simplified(self, sentence):
        sum = 0
        result = []
        types = ['noun','verb','adp','.','det','adj','adv','pron','conj','prt','num','x']
        for elem in sentence:
            max = -1
            for elem1 in types:
                Solver.emission_prob.append(((elem,elem1),Solver.tr[(elem,elem1)]/(Solver.tr1[elem1] * 1.0)))
                if max < Solver.tr[(elem,elem1)]/(Solver.tr1[elem1] * 1.0):
                   max_elem = elem1
                   max = Solver.tr[(elem,elem1)]/(Solver.tr1[elem1] * 1.0)
            result.append(max_elem)
#            print max
            if max != 0:
               sum = sum + math.log(max)
        Solver.simple_posterior = sum
#        print Solver.emission_prob
        Solver.simple_result = result
        return result

    def complex_mcmc(self, sentence):
        samples = []
        types = ['noun','verb','adp','.','det','adj','adv','pron','conj','prt','num','x']
        samples.append(Solver.simple_result)
        for i in range(0,50):
            last = samples[-1]
            particle = ['x' for x in range(0,len(sentence))]
            for k in range(0,len(sentence)):
                p1 = []
                for m in range(0,len(types)):
                    if k == 0:
                       p1.append(self.find_emission1(sentence[k],types[m]))
                    elif k == 1:
                       p1.append(self.find_trans1(last[k-1],types[m]) * self.find_emission1(sentence[k],types[m]))
                    else:
                       to1 = Solver.tr7[(last[k-2],last[k-1],types[m])] * 1.0
#                       print to1
                       to2 = Solver.tr1[types[m]] * 1.0
#                       print to2
                       to3 = to1/to2
                       p1.append(self.find_trans1(last[k-1],types[m]) * self.find_emission1(sentence[k],types[m]))
                
                bal = 1.0 - sum(p1)
                s = sum(p1)
                p1 = [x+((((x/s)*100)*bal)/100) for x in p1]
                t = np.random.choice(types , 1, p = [x for x in p1])
                particle[k] = t[0]
            samples.append(particle)
#        print samples
        result = []
        for i in range(0,len(sentence)):
            ex = []
            for j in range(0,50):
                ex.append(samples[j][i])
            result.append(Counter(ex).most_common(1)[0][0])

        return result

    def hmm_viterbi(self, sentence):

        types = ['noun','verb','adp','.','det','adj','adv','pron','conj','prt','num','x']
        viterbi_matrix  = [[None for x in range(len(types))] for y in range(len(sentence)+1)]
        for i in range(len(sentence) + 1):
            if i == 0:
               for j in range(0,len(types)):
#                   print self.find_emission(sentence[i],types[j]),sentence[i],types[j]
#                   print self.find_trans('start',types[j]),'start',types[j]
                   viterbi_matrix[i][j] = (self.find_emission(sentence[i],types[j]) + self.find_trans('start',types[j]),'start')
            elif i == len(sentence):
                 for j in range(0,len(types)):
                   pos1 = []
                   for k in range(0,len(types)):
                       pos1.append(self.find_emission(sentence[i-1],types[j]) + viterbi_matrix[i-1][k][0] + self.find_trans('end',types[j]))
#                       print self.find_emission(sentence[i-1],types[j]),sentence[i-1],types[j]
#                       print viterbi_matrix[i-1][k]
#                       print self.find_trans('end',types[j]),'end',types[j]
                   max_prob = max(pos1)
                   viterbi_matrix[i][j] = (max_prob,types[pos1.index(max_prob)])
            else:
               for j in range(0,len(types)):
                   pos1 = []
                   for k in range(0,len(types)):
                       pos1.append(self.find_emission(sentence[i],types[j]) + viterbi_matrix[i-1][k][0] + self.find_trans(types[k],types[j]))
#                       print self.find_emission(sentence[i],types[j]),sentence[i],types[j]
#                       print viterbi_matrix[i-1][k]
#                       print self.find_trans(types[k],types[j]),types[k],types[j]
                   max_prob = max(pos1)
                   viterbi_matrix[i][j] = (max_prob,types[pos1.index(max_prob)])
        
        sum = 0
        result = []        
        for i in range(0,len(sentence)+1):
            pos2 = []
            for j in range(0,len(types)):
                pos2.append(viterbi_matrix[i][j][0])
            result.append(viterbi_matrix[i][pos2.index(max(pos2))][1])
#            print viterbi_matrix[i][pos2.index(max(pos2))][0]
            if viterbi_matrix[i][pos2.index(max(pos2))][0] != 0:
               sum = sum + viterbi_matrix[i][pos2.index(max(pos2))][0]    
#        print result[1:]
        Solver.veterbi_posterior = sum    
         
#        print viterbi_matrix
        return result[1:]
        

                    


    # This solve() method is called by label.py, so you should keep the interface the
    #  same, but you can change the code itself. 
    # It should return a list of part-of-speech labelings of the sentence, one
    #  part of speech per word.
    #
    def solve(self, model, sentence):
        if model == "Simple":
            return self.simplified(sentence)
        elif model == "Complex":
            return self.complex_mcmc(sentence)
        elif model == "HMM":
            return self.hmm_viterbi(sentence)
        else:
            print("Unknown algo!")

