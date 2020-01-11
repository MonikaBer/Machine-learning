import random
from sklearn import svm
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB

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

averageSVM = []
averageBayes = []

k = 10
size = int(len(y)/k)

#number of set to test quality of prediction, other sets are training sets
testSet = 0
while testSet < k:
    #testing SVM method using different test sets
    clf = svm.SVC()      #SVM's constructor
    gnb = GaussianNB()   #Bayes's constructor
    X_train = []
    Y_train = []
    for setNr in range(k):
        if setNr != testSet:
            i = setNr * size
            if setNr != 9:
                finish = i + size
            else:
                finish = len(y)

            while i < finish:
                X_train.append(x[i])
                Y_train.append(y[i])
                i+=1

            setNr+=1

    X_test = []
    Y_test = []
    i = testSet * size
    finish = i + size
    while i < finish:
        X_test.append(x[i])
        Y_test.append(y[i])
        i+=1

    #training SVM and Bayes, and prediction
    resultOfPredictionForSVM = []
    clf.fit(X_train,Y_train)
    resultOfPredictionForSVM = clf.predict(X_test)

    resultOfPredictionForBayes = []
    resultOfPredictionForBayes = gnb.fit(X_train, Y_train).predict(X_test)

    numberOfHitsForSVM = 0
    numberOfHitsForBayes = 0
    i = 0
    while i < len(Y_test):
        if resultOfPredictionForSVM[i] == Y_test[i]:
            numberOfHitsForSVM+=1
        if resultOfPredictionForBayes[i] == Y_test[i]:
            numberOfHitsForBayes+=1
        i+=1

    resultForSVM = numberOfHitsForSVM/len(Y_test)
    resultForBayes = numberOfHitsForBayes/len(Y_test)

    averageSVM.append(resultForSVM)
    averageBayes.append(resultForBayes)

    testSet+=1  #change of number of test set

sumForSVM = 0
sumForBayes = 0
i = 0
while i < len(averageSVM):
    sumForSVM += averageSVM[i]
    sumForBayes += averageBayes[i]
    i+=1

resultForSVM = sumForSVM/len(averageSVM)
resultForBayes = sumForBayes/len(averageBayes)

print("Result for SVM", resultForSVM*100, "%")
print("Result for Bayes", resultForBayes*100, "%")
