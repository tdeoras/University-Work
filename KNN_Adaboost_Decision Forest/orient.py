#!/usr/bin/env python
import numpy as np
from collections import Counter
import math
import collections
import copy
import random
import pickle as pickle
import sys
import pandas as pd
import time
import csv 
import heapq
from collections import defaultdict



train_test = sys.argv[1]
file_name = sys.argv[2]
model_file = sys.argv[3]
model = sys.argv[4]

if model == 'forest':

  if train_test == 'train':

      train_file = file_name
#      test_file = 'test-data.txt'

      def readData(path,data):
          #creates vectors of the form [orientation, vectors....]
          #orientation is class variable
          vectors={}
          f=open(path,'r')
          for line in f:
              line=line.strip()
              if data=='train':
                 identity=(line.split(' ')[0],int(line.split(' ')[1]))
              else:
                 identity=(line.split(' ')[0],int(line.split(' ')[1]))
              vectors[identity]=np.array(list(map(int,line.split(' ')[2:])))
          return vectors


      train1 =  readData(train_file,'train')
#      test1 = readData(test_file,'test')

      #print train1[('train/10008667845.jpg',0)][0]
      #Converts values form continious to discrete
      def quantify(vectors):
          for elem in vectors:
              temp = []
              for elem1 in vectors[elem]:
                  if elem1 > 85:
                     p = 'low'
                  elif elem1 >= 85 and elem1 <= 170:
                     p = 'medium'
                  else:
                     p = 'high'
                  temp.append(p)
              vectors[elem]=np.array(temp)
          return vectors 
       
      new_train = quantify(train1)
      
      #print new_train

      labels = [0,90,180,270]
      attributes = [x for x in range(0,192)]

      #print labels 
      #print attributes
      #Calculates Entropy for Column
      def entropy(column,dataset2):
          temp = []
          tr = Counter()
          tr1 = Counter()
          for elem in dataset2:
              temp.append(dataset2[elem][column])
              tr[dataset2[elem][column]] += 1
              tr1[(dataset2[elem][column],elem[1])] += 1
          temp1 = np.asarray(temp)
          elements = np.unique(temp1)
          counts = []
          elements = elements.tolist()
      #    print elements
          for elem in elements:
              counts.append(tr[elem])
          counts = [x * 1.0 for x in counts]
      #    print sum(counts)
      #    print sum(tr1.itervalues())
      #    entropy = np.sum([(-counts[i]/np.sum(counts))*np.log2(counts[i]/np.sum(counts)) for i in range(len(elements))])
          result = []
          for i in elements:
              t1 = (tr[i] * 1.0)/sum(counts)
      #        print t1
      #        print ((-tr1[i,0] * 1.0)/(tr[i] * 1.0))
              r1 = []
              for j in labels:
                  if tr1[i,j] != 0 and tr[i] != 0:
                       t2 = ((-tr1[i,j] * 1.0)/(tr[i] * 1.0)) * math.log(((tr1[i,j] * 1.0)/(tr[i] * 1.0)),2)
                       r1.append(t2)
              t4 = sum(r1)
              t3 = t1 * t4
              result.append(t3)
          return sum(result)
      #    return entropy

      #print entropy(190)
                 
      #elements,counts = np.unique(new_train[:,0],return_counts = True)

      #print elements,counts
      #Lowest entropy among all the given columns
      def find_lowest_entropy(predicates,dataset1):
          max = -1
          for elem in predicates:
              if max < entropy(elem,dataset1):
                 max = entropy(elem,dataset1)
                 max_elem = elem
          return max_elem

      #p = [x for x in range(0,20)]

      #print entropy(1,new_train)
      #print entropy(2)
      #print entropy(3)
      #print entropy(4)
      #print find_lowest_entropy(p)     



      #Tree data structure
      class Node(object):
          def __init__(self, data):
              self.data = data
              self.children = []
              self.answer = None
              self.br = None

          def add_child(self, obj):
              self.children.append(obj)

      random_attributes = 14
      no_of_trees = 100

      def dataset_change(dataset,label,col):
          train1 = copy.deepcopy(dataset)
          for elem1 in list(train1.keys()):
              if train1[elem1][col] != label:
                 del train1[elem1]
          return train1

      def dataset_end(dataset):
          temp = []
          for elem in dataset:
              temp.append(elem[1])
          if len(set(temp)) == 1:
             return temp[0]
          else:
             return -1



      #d = list(new_train)
      #keys = random.sample(d, 10000)
      #print keys
      #print keys

      def dataset_initial(dataset,predicates,keys):
          train2 = copy.deepcopy(dataset)
          for elem in list(train2.keys()):
              if elem not in keys:
                 del train2[elem]
          return train2


      def end_answer(dataset):
          data1 = copy.deepcopy(dataset)
          tr3 = Counter()
          for elem in data1:
              tr3[elem[1]] += 1
      #    print tr3       
          return (tr3.most_common(1))[0][0]

      def empty_dataset(dataset,col):
          temp = []
          for elem in dataset:
              temp.append(dataset[elem][col])
          if len(set(temp)) == 1:
             return end_answer(dataset)
          else:
             return -1

      #data1 = dataset_initial(new_train,p,keys)
      #print data1
      #print find_lowest_entropy(p,data1)
      #print find_lowest_entropy(p,new_train)
      #print len(dataset_change(data1,'low',0))
      #print len(data1)
      #print len(new_train)

      atr = ['low','medium','high']
      #Recursive algo for decision tree construction as given in slides
      def Decision_Tree(data,predicate,decision):
          a1 = dataset_end(data)    
          if a1 != -1:
             temp = Node(a1)
             temp.answer = a1
             temp.br = decision
      #       print temp.data,temp.answer
             return temp
          if not predicate:
             temp = Node(-1)
      #       print end_answer(data)
             temp.answer = end_answer(data)
             temp.br = decision
      #       print temp.data,temp.answer
             return temp
          a = find_lowest_entropy(predicate,data)
          root = Node(a)
          root.br = decision
      #    print root.data,root.br
          predicate.remove(a)
          for elem in atr:
              temp_pred = copy.deepcopy(predicate)
              if len(dataset_change(data,elem,a)) > 0:
                 root.add_child(Decision_Tree(dataset_change(data,elem,a),temp_pred,elem))
              else:
                 temp = Node(-1)
                 temp.br = elem
      #       print end_answer(data)                                                                                                                                                                             
                 temp.answer = -1
      #           print temp.data,temp.answer
                 root.add_child(temp)
          return root

              
      #m = Decision_Tree(data1,p,'root')


      #test1 = new_test[('test/10107730656.jpg',180)]
      #print test1

      #walking tree according test data
      def walk(root,test1):
          answer = root.answer
          if answer == None:
             branch = test1[root.data]
             for elem in root.children:
                 if elem.br == branch:
      #              print branch
                    return walk(elem,test1)
          else:
      #      print answer
            return answer







      def travesal(root):
          fringe = []
          fringe.append(root)
          while len(fringe) > 0:
                temp = fringe.pop()
                print(temp.data,temp.br)
                if temp.answer:
                   print(temp.data,temp.answer)
                else:
                   for elem in temp.children:
                       fringe.insert(0,elem)



      #x = dataset_change(p,new_train,'high',0)
      #print x
      #print dataset_end(x)
      #print dataset_initial(new_train,p)

      #travesal(m)
      #print '--------------------------------------------------'
      #t = walk(m,test1)
      #print t


      #for elem in new_test:
      #    print 'Actual Label :'
      #    print elem[1]
      #    tempcounter = Counter()

      forest = []

      start = time.time()
      for i in range(10):
          pf = []
          for k in range(20):
              temp = random.randint(0,191)
              if temp not in pf:
                 pf.append(temp)
              
          df = list(new_train)
          keysf = random.sample(df, 20000)
          dataf = dataset_initial(new_train,pf,keysf)
              
          tree = Decision_Tree(dataf,pf,'root')
          print(tree)
          forest.append(tree)
      
      end = time.time()  
      print('Time :')
      print((end-start))
      


      #Pickle to store data structure in a file
      filehandler = open(model_file, 'w')
      pickle.dump(forest, filehandler)
      filehandler.close()

  if train_test == 'test':
      
      def walk(root,test1):
          answer = root.answer
          if answer == None:
             branch = test1[root.data]
             for elem in root.children:
                 if elem.br == branch:
      #              print branch                                                                                                                                                                           
                    return walk(elem,test1)
          else:
      #      print answer                                                                                                                                                                                   
            return answer
      

      class Node(object):
          def __init__(self, data):
              self.data = data
              self.children = []
              self.answer = None
              self.br = None

          def add_child(self, obj):
              self.children.append(obj)

      def readData(path,data):
          #creates vectors of the form [orientation, vectors....]
          #orientation is class variable
          vectors={}
          f=open(path,'r')
          for line in f:
              line=line.strip()
              if data=='train':
                 identity=(line.split(' ')[0],int(line.split(' ')[1]))
              else:
                 identity=(line.split(' ')[0],int(line.split(' ')[1]))
              vectors[identity]=np.array(list(map(int,line.split(' ')[2:])))
          return vectors


      test_file = file_name
      test1 = readData(test_file,'test')

      def quantify(vectors):
          for elem in vectors:
              temp = []
              for elem1 in vectors[elem]:
                  if elem1 > 85:
                     p = 'low'
                  elif elem1 >= 85 and elem1 <= 170:
                     p = 'medium'
                  else:
                     p = 'high'
                  temp.append(p)
              vectors[elem]=np.array(temp)
          return vectors 
       
      
      new_test = quantify(test1)
      #print new_train

      labels = [0,90,180,270]
      attributes = [x for x in range(0,192)]

   




      filehandler1 = open(model_file, 'r')
      forest1 = pickle.load(filehandler1)
      print(forest1)

      filehandler2 = open('output_forest.txt', 'w+')


      total = len(new_test)
      count = 0 
      
      for elem in new_test:
          print('Actual Label')
          print(elem[1])
          l1 = elem[1]
          tempcounter = Counter()
          for elem1 in forest1:
              answer = walk(elem1,new_test[elem])
              tempcounter[answer] += 1
          print('Estimated Label:')
          size = len(tempcounter)
          l2 = 0
          for i in range(0,size):
              if (tempcounter.most_common(size))[i][0] != -1:
                  print((tempcounter.most_common(size))[i][0])
                  l2 = (tempcounter.most_common(size))[i][0] 
                  break   
          if l1 == l2:
             count = count + 1
          out = str(elem[0]) + ' ' + str(l2)
          filehandler2.write(out + '\n') 


      print('Accuracy :')
      count = count * 1.0
      total = total * 1.0
      l3 = (count/total) * 100.0 
      print(l3)
              
      #        answer = walk(tree,new_test[elem])
      #        print answer
              
      #        tempcounter[answer] += 1
          
      #    print 'Actual Label :'
      #    print elem[1]
      #    print 'Estimated Label :'
      #    for i in range(0,2):
      #        if (tempcounter.most_common(2))[i][0] != -1:
      #           print (tempcounter.most_common(2))[i][0]    
      #           break


if model == 'nearest':
  
  if train_test == 'train':

     tr = file_name
     trn = pd.read_csv(tr,sep= '\s+',header = None)

     trn = trn.iloc[1:16000][:]
     tr_img=[]
     tr_y_lbl=[]
     tr_img=trn.iloc[:][0].values
     tr_y_lbl= trn.iloc[:][1].values
     
 
     del trn[0]
     del trn[1]
     
     trn.columns = list(range(trn.shape[1]))
     trn = trn.values 

     model_pram = [trn,tr_y_lbl,tr_img]

     filehandler = open(model_file,'wb')
     pickle.dump(model_pram,filehandler)
     filehandler.close()

  if train_test == 'test':

     filehandler1 = open(model_file, 'rb')
     model_pram = pickle.load(filehandler1)
     trn = model_pram[0]
     tr_y_lbl = model_pram[1]
     tr_img = model_pram[2]

     ts = file_name
     tst=pd.read_table(ts, sep= '\s+',header=None)

     tst_y_lbl=[]

     tst_y_lbl=tst.iloc[:][1].values
     tst_img=tst.iloc[:][0].values

     del tst[1]
     del tst[0]

     tst = tst.values

     def KNN(tst,trn,tr_y_lbl):
         final_value = []
         for i in range(0,len(tst)):
             euclidian_dist = []
             tst_values=tst[i]
             prd_y_dist_lbl = []
             prd_y_lbl = []
             for trn_values in trn:
                 # euclidian distance formula refrenced from knn data science blog
                 knn_d = math.sqrt(np.sum(np.power((trn_values - tst_values), 2)))
                 euclidian_dist.append(knn_d)
        
             k_nbr = 11
             prd_y_dist_lbl=tuple(zip(euclidian_dist,tr_y_lbl))
             sort_tpl = sorted(prd_y_dist_lbl, key=lambda y: y[0])
             for value in range(0, k_nbr):
                 prd_y_lbl.append(sort_tpl[value][1])
             vote = max(set(prd_y_lbl), key=prd_y_lbl.count)
             final_value.append(vote)
         output(tr_img,final_value,tr_y_lbl)

      
     def output(tr_img,final_value,tr_y_lbl):
         output_tpl=[]
         output_tpl=list(zip(tst_img,final_value))


         array_final_value=np.array(final_value)
         array_tst_y_lbl=np.array(tst_y_lbl)
         score=np.sum(array_final_value==array_tst_y_lbl)
         accuracy=(score/float(len(tst_y_lbl)))*100.0
         print(("Accuracy score: {}".format(accuracy)))
         with open('output_nearest.txt', 'w') as write_file:
              write_file.write('\n'.join('%s %s' % line for line in output_tpl))

     start_time=time.time()
     KNN(tst,trn,tr_y_lbl)
     print(("Time Taken: {}".format(time.time()-start_time)))






class Adaboost():
    def __init__(this, training_data=None, testing_data=None):
        this.training , this.testing = (training_data, testing_data)
        
        this.learners = [this.learner1, this.learner2]

    #function to read data file
    def prepare_data(this, filename):
        this.pixels , this.rotation , this.ids = ([], [], [])
        
        lines = open(filename).readlines()
        for line in lines:
            line = line.split(" ")
            
            this.ids.append(line[0])
            
            this.rotation.append(int(line[1]))
            
            this.pixels.append([int(x) for x in line[2:]])         
            
        return this.pixels, this.rotation, this.ids

    #blue
    def learner1(this, train):
        out = list()
        for data in train:

            top = sum(data[2:24:3])
            right= sum(data[23:192:24])
            bottom=  sum(data[170:192:3])
            left=   sum(data[2:192:24])
            
            #options = defaultdict(lambda: out.append(270), {'this': 1, 'that': 2, 'there': 3})

            x=  max([top, right, bottom, left])
            
            if x == top: out.append(0)
            elif x == bottom: out.append(180)
            elif x == right: out.append(90)
            elif x == left: out.append(270)
            else : continue
            
        return out

    #brown
    def learner2(this, train):
        out = list()
        for data in train:
            top=sum(data[0:23:3])
            right =sum(data[21:192:24])
            bottom= sum(data[168:192:3])
            left= sum(data[0:192:24])
            x=  max([top, right, bottom, left])
            if x == top: out.append(180)
            elif x == bottom: out.append(0)
            elif x  == right:out.append(270)
            elif x == left: out.append(90)
            else : continue
        return out

    # function to compare the performance of each classifier on the train set
    def comp_learner(this, train, learners):
        train_rot= this.prepare_data(this.training)
        this.train_rotation = train_rot[1]
        out = {i:0 for i in learners}
        for learner in learners:
            
            pred = learner(train)
            correct ,i =(0,0)
            
            while i <len(train):
                if pred[i] == this.train_rotation[i]:
                    correct += this.obs_weights[i]
                i+=1
            out[learner] = correct
        return max(out, key=out.get)

    #training adaboost
    def train(this, train):
        this.obs_weights = [1/float(len(train))]*len(train)
        this.learners = [this.learner1, this.learner2]
        hypothesis_wt , test = {}, {}
        
        while len(this.learners) > 0:
            learner = this.comp_learner(train, this.learners)
            error = 0
            pred1 = learner(train)
            i=0
            while i < len(train):
                if pred1[i] != this.train_rotation[i]:
                    error += this.obs_weights[i]
                final_error = error
                if pred1[i] == this.train_rotation[i]:
                    this.obs_weights[i] = this.obs_weights[i]*(final_error/(1-final_error))
                i+=1
            this.obs_weights = [float(i)/sum(this.obs_weights) for i in this.obs_weights]
            hypothesis_wt[learner] = math.log((1-final_error)/final_error)
            this.learners.remove(learner)
        return hypothesis_wt

    #function to predict for test file; paramters: test-file name
    def test(this, test_file, model_file):
        this.test=test_file
        pixels, rotation, ids = this.prepare_data(this.test)
        new ,new_weight = {} , {}
        lines = open(model_file).readlines() #reading weights from text file
        for line in lines:
            line = line.split(" ")
            px=line[0]
            py=line[1]
            new[px] = float(py[:-1])

        
        for i in new:
            if i == 'paramx':
                new_weight[this.learner1] = new[i]
            elif i == 'paramy':
                new_weight[this.learner2] = new[i]
            else: continue

        out = {i: [] for i in range(len(pixels))}
        for learner in this.learners:
           
            for i, j in enumerate(learner(pixels)):
                out[i].append((j, new_weight[learner]))
        for key, value in list(out.items()):
            test = {}
            for p,q in value:
                if p not in test:
                    test[p] = q
                else:
                    test[p] += q
            out[key] = max(test, key = test.get)
        with open("output_adaboost.txt", 'w') as output_file:
            start=0
            for i,j in enumerate(ids,start=0):
                output_file.write('%s %d\n' % (j, out[i]))
        
        return out




    #Calculates overall accuracy
    def get_accuarcy(this, actual, predicted):
        
        i=0
        count = 0
        while i < (len(actual)):
            if actual[i] == predicted[i]:
                count += 1
            i+=1
            accuracy= float(count)/len(actual)*100
        return accuracy




if model == 'adaboost':

   if train_test == 'train':

        trial = Adaboost(file_name, None)
        trial.training = file_name
       
        weights = trial.train(trial.prepare_data(trial.training)[0])
        weight_values = list(weights.values())
        for i in weights:
            weights[i] += 10
        
        with open(model_file, 'w') as myfile:
            for i in weights:
                if i != trial.learner1:
                    myfile.write('%s %.9f\n' % ('paramy', weights[i]))
                if i != trial.learner2:
                    myfile.write('%s %.9f\n' % ('paramx', weights[i]))
      
    

   if train_test == 'test':
      

        trial = Adaboost(None, file_name)
        
        test_rotation = trial.prepare_data(file_name)[1]
        learners = [trial.learner1, trial.learner2]
        acc=trial.get_accuarcy(test_rotation, trial.test(file_name, model_file))
        print(("Accuracy on test set:  " + str( round(acc,2)) + "%"))




if model == 'best':

  if train_test == 'train':

     tr = file_name
     trn = pd.read_csv(tr,sep= '\s+',header = None)

     trn = trn.iloc[1:16000][:]
     tr_img=[]
     tr_y_lbl=[]
     tr_img=trn.iloc[:][0].values
     tr_y_lbl= trn.iloc[:][1].values


     del trn[0]
     del trn[1]

     trn.columns = list(range(trn.shape[1]))
     trn = trn.values

     model_pram = [trn,tr_y_lbl,tr_img]

     filehandler = open(model_file,'wb')
     pickle.dump(model_pram,filehandler)
     filehandler.close()


  if train_test == 'test':

     filehandler1 = open(model_file, 'rb')
     model_pram = pickle.load(filehandler1)
     trn = model_pram[0]
     tr_y_lbl = model_pram[1]
     tr_img = model_pram[2]

     ts = file_name
     tst=pd.read_table(ts, sep= '\s+',header=None)

     tst_y_lbl=[]

     tst_y_lbl=tst.iloc[:][1].values
     tst_img=tst.iloc[:][0].values

     del tst[1]
     del tst[0]

     tst = tst.values

     def KNN(tst,trn,tr_y_lbl):
         final_value = []
         for i in range(0,len(tst)):
             euclidian_dist = []
             tst_values=tst[i]
             prd_y_dist_lbl = []
             prd_y_lbl = []
             for trn_values in trn:
                 # euclidian distance formula refrenced from knn data science blog                                                                                                                          
                 knn_d = math.sqrt(np.sum(np.power((trn_values - tst_values), 2)))
                 euclidian_dist.append(knn_d)



             k_nbr = 11
             prd_y_dist_lbl=tuple(zip(euclidian_dist,tr_y_lbl))
             sort_tpl = sorted(prd_y_dist_lbl, key=lambda y: y[0])
             for value in range(0, k_nbr):
                 prd_y_lbl.append(sort_tpl[value][1])
             vote = max(set(prd_y_lbl), key=prd_y_lbl.count)
             final_value.append(vote)
         output(tr_img,final_value,tr_y_lbl)


     def output(tr_img,final_value,tr_y_lbl):
         output_tpl=[]
         output_tpl=list(zip(tst_img,final_value))


         array_final_value=np.array(final_value)
         array_tst_y_lbl=np.array(tst_y_lbl)
         score=np.sum(array_final_value==array_tst_y_lbl)
         accuracy=(score/float(len(tst_y_lbl)))*100.0
         print(("Accuracy score: {}".format(accuracy)))
         with open('output_best.txt', 'w') as write_file:
              write_file.write('\n'.join('%s %s' % line for line in output_tpl))

     start_time=time.time()
     KNN(tst,trn,tr_y_lbl)
     print(("Time Taken: {}".format(time.time()-start_time)))











