import random
from sklearn import svm

file = open("data_banknote_authentication.txt", "r")
list = []

for line in file:
    line = line.strip('\n')
    numbers = line.split(",")
    tuple = (float(numbers[0]), float(numbers[1]), float(numbers[2]), float(numbers[3]), int(numbers[4]))
    list.append(tuple)
file.close()

#cross-validation
random.shuffle(list)

x = []  #parameters
y = []  #class

i = 0
while i < len(list):
    row = []
    for j in range(4):
        row.append(list[i][j])
    x.append(row)
    y.append(list[i][4])
    i+=1

average = []

k = 10
size = int(len(y)/k)

#number of set to test quality of prediction, other sets are training sets
testSet = 0
while testSet < k:
    #testing SVM method using different test sets
    clf = svm.SVC()
    X = []
    Y = []
    for setNr in range(k):
        if setNr != testSet:

            i = setNr * size
            if setNr != 9:
                finish = i + size
            else:
                finish = len(y)

            while i < finish:
                X.append(x[i])
                Y.append(y[i])
                i+=1

            setNr+=1

    #trening of SVM method using training set
    clf.fit(X,Y)

    #test prediction using test set
    X = []
    Y = []
    i = testSet * size
    finish = i + size
    while i < finish:
        X.append(x[i])
        Y.append(y[i])
        i+=1

    resultOfPrediction = []
    resultOfPrediction = clf.predict(X)

    numberOfHits = 0
    i = 0
    while i < len(Y):
        if resultOfPrediction[i] == Y[i]:
            numberOfHits+=1
        i+=1

    result = numberOfHits/len(Y)
    average.append(result)

    testSet+=1  #change of number of test set

sum = 0
i = 0
while i < len(average):
    sum += average[i]
    i+=1

resultForSVM = sum/len(average)
print("Result for SVM", resultForSVM*100, "%")
