

file = open("data_banknote_authentication.txt", "r")
x = []  #parameters
y = []  #class

for line in file:
    line = line.strip('\n')
    numbers = line.split(",")
    row = []
    for i in range(4):
        row.append(numbers[i])
    x.append(row)
    y.append(numbers[4])
file.close()





