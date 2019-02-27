import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

dataset = pd.read_csv('/home/tejasdeoras/Downloads/adult.csv')
X = dataset.iloc[:, :-1].values
Y = dataset.iloc[:, 14].values
dataset = dataset[dataset['native.country'] != '?']
dataset = dataset[dataset['age'] != 0]
dataset = dataset[dataset['workclass'] != '?']
dataset = dataset[dataset['fnlwgt'] != 0]
dataset = dataset[dataset['education'] != '?']
dataset = dataset[dataset['education.num'] != 0]
dataset = dataset[dataset['occupation'] != '?']
dataset = dataset[dataset['relationship'] != '?']
dataset = dataset[dataset['race'] != '?']
dataset = dataset[dataset['sex'] != '?']
bins = [0,14,24,64,100]
labels = ['Child','Youth','Adult','Senior']
dataset.age = pd.cut(dataset.age, bins=bins, labels=labels)
del dataset['fnlwgt']
dataset.rename(columns = {'capital.gain':'capitalgain'}, inplace = True)
dataset.rename(columns = {'capital.loss':'capitalloss'}, inplace = True)
dataset.rename(columns = {'hours.per.week':'hoursperweek'}, inplace = True)
dataset.rename(columns = {'native.country':'nativecountry'}, inplace = True)
bins1 = [-1,1,25000,50000,100000]
labels1 = ['none','low','moderate','high']
dataset.capitalgain = pd.cut(dataset.capitalgain, bins=bins1, labels=labels1)
bins2 = [-1,1,1000,2000,3000,4500]
labels2 = ['none','low','moderate','high','veryhigh']
dataset.capitalloss = pd.cut(dataset.capitalloss, bins=bins2, labels=labels2)
print(dataset)



/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

rating_probs1 = dataset.groupby('age').size().div(len(dataset))
print(rating_probs1)
conditional_prob1 = dataset.groupby(['income', 'age']).size().div(len(dataset)).div(rating_probs1, axis=0, level='age')
print(conditional_prob1)
rating_probs2 = dataset.groupby('workclass').size().div(len(dataset))
print(rating_probs2)
conditional_prob2 = dataset.groupby(['income', 'workclass']).size().div(len(dataset)).div(rating_probs2, axis=0, level='workclass')
print(conditional_prob2)
rating_probs3 = dataset.groupby('education').size().div(len(dataset))
print(rating_probs3)
conditional_prob3 = dataset.groupby(['income', 'education']).size().div(len(dataset)).div(rating_probs3, axis=0, level='education')
print(conditional_prob3)
rating_probs4 = dataset.groupby('marital.status').size().div(len(dataset))
print(rating_probs4)
conditional_prob4 = dataset.groupby(['income', 'marital.status']).size().div(len(dataset)).div(rating_probs4, axis=0, level='marital.status')
print(conditional_prob4)
rating_probs5 = dataset.groupby('occupation').size().div(len(dataset))
print(rating_probs5)
conditional_prob5 = dataset.groupby(['income', 'occupation']).size().div(len(dataset)).div(rating_probs5, axis=0, level='occupation')
print(conditional_prob5)
rating_probs6 = dataset.groupby('relationship').size().div(len(dataset))
print(rating_probs6)
conditional_prob6 = dataset.groupby(['income', 'relationship']).size().div(len(dataset)).div(rating_probs6, axis=0, level='relationship')
print(conditional_prob6)
rating_probs7 = dataset.groupby('race').size().div(len(dataset))
print(rating_probs7)
conditional_prob7 = dataset.groupby(['income', 'race']).size().div(len(dataset)).div(rating_probs7, axis=0, level='race')
print(conditional_prob7)
rating_probs8 = dataset.groupby('sex').size().div(len(dataset))
print(rating_probs8)
conditional_prob8 = dataset.groupby(['income', 'sex']).size().div(len(dataset)).div(rating_probs8, axis=0, level='sex')
print(conditional_prob8)
rating_probs9 = dataset.groupby('capitalgain').size().div(len(dataset))
print(rating_probs9)
conditional_prob9 = dataset.groupby(['income', 'capitalgain']).size().div(len(dataset)).div(rating_probs9, axis=0, level='capitalgain')
print(conditional_prob9)
rating_probs10 = dataset.groupby('capitalloss').size().div(len(dataset))
print(rating_probs10)
conditional_prob10 = dataset.groupby(['income', 'capitalloss']).size().div(len(dataset)).div(rating_probs10, axis=0, level='capitalloss')
print(conditional_prob10)





cp1 = ["Youth","Adult","Senior"]
f1 = list(zip(cp1,conditional_prob1[3:]))
print(f1)
cp2 = ["Federal-gov","Local-gov","Private","Self-emp-inc","Self-emp-not-inc","State-gov","Without-pay"]
f2 = list(zip(cp2,conditional_prob2[7:]))
print(f2)
cp3 = ["10th","11th","12th","1st-4th","5th-6th","7th-8th","9th","Assoc-acdm","Assoc-voc","Bachelors","Doctorate","HS-grad","Masters","Prof-school","Some-college"]
f3 = list(zip(cp3,conditional_prob3[16:]))
print(f3)
cp4 = ["Divorced","Married-AF-spouse","Married-civ-spouse","Married-spouse-absent","Never-married","Separated","Widowed"]
f4 = list(zip(cp4,conditional_prob4[7:]))
print(f4)
cp5 = ["Adm-clerical","Armed-Forces","Craft-repair","Exec-managerial","Farming-fishing","Handlers-cleaners","Machine-op-inspct","Other-service","Priv-house-serv","Prof-specialty","Protective-serv","Sales","Tech-support","Transport-moving"]
f5 = list(zip(cp5,conditional_prob5[14:]))
print(f5)
cp6 = ["Husband","Not-in-family","Other-relative","Own-child","Unmarried","Wife"]
f6 = list(zip(cp6,conditional_prob6[6:12]))
print(f6)
cp7 = ["Amer-Indian-Eskimo","Asian-Pac-Islander","Black","Other","White"]
f7 = list(zip(cp7,conditional_prob7[5:10]))
print(f7)
cp8 = ["Female","Male"]
f8 = list(zip(cp8,conditional_prob8[2:4]))
print(f8)
cp9 = ["none","low","moderate","high"]
f9 = list(zip(cp9,conditional_prob9[3:7]))
print(f9)
cp10 = ["none","low","moderate","high","veryhigh"]
f10 = list(zip(cp10,conditional_prob10[5:10]))
print(f10)


def takeSecond(elem):
    return elem[1]
print("\n")
finallist = f1 + f2 + f3 + f4 + f5 + f6 + f7 + f8 + f9 + f10;
finallist.sort(key=takeSecond)
print("\n")
print("\n")
print(finallist)
print("\n")
print(len(finallist))
fwgt = []

dataset_test = dataset[dataset.income == ">50K"]
print(dataset_test)
for i in range(0,7508):
    wgt=0
    for j in range(0,67):
        if dataset_test.iloc[i]['age'] == finallist[j][0]:
            wgt = wgt + j
        elif dataset_test.iloc[i]['workclass'] == finallist[j][0]:
            wgt = wgt + j
        elif dataset_test.iloc[i]['education'] == finallist[j][0]:
            wgt = wgt + j
        elif dataset_test.iloc[i]['marital.status'] == finallist[j][0]:
            wgt = wgt + j
        elif dataset_test.iloc[i]['occupation'] == finallist[j][0]:
            wgt = wgt + j
        elif dataset_test.iloc[i]['relationship'] == finallist[j][0]:
            wgt = wgt + j
        elif dataset_test.iloc[i]['race'] == finallist[j][0]:
            wgt = wgt + j
        elif dataset_test.iloc[i]['sex'] == finallist[j][0]:
            wgt = wgt + j
        elif dataset_test.iloc[i]['age'] == finallist[j][0]:
            wgt = wgt + j
        elif dataset_test.iloc[i]['capitalgain'] == finallist[j][0]:
            wgt = wgt + j
    
    print(wgt)
    print(i)
    fwgt.append(wgt)

print("/////////////////////////////////////////////////////////////////////////")
print(len(fwgt))


fwgt.sort()

q75, q25 = np.percentile(fwgt, [75 ,25])
iqr = q75 - q25

print("//////////////////////////")
print(iqr)

minl = q25 - 1.5*iqr
maxl = q75 + 1.5*iqr

count = 0;

for k in range(0,7508):
    if fwgt[k] < minl or fwgt[k] > maxl:
        count = count + 1;
        print(dataset_test.iloc[k])
        

print(count);
/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////




    
        
            
            









        

























