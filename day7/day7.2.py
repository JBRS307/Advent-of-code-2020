def prepareArr(arr):
    compareArr = ['2', '3', '4', '5', '6', '7', '8', '9']
    returnArr = []
    for line in arr:
        line[1] = line[1].split(", ")
        for i in range(len(line[1])):
            if line[1][i][0] == '1':
                line[1][i] = line[1][i].replace(" bag", '')
                line[1][i] = line[1][i].replace(".\n", '')
                #print(line[1][i])
            elif line[1][i][0] in compareArr:
                line[1][i] = line[1][i].replace(" bags", '')
                line[1][i] = line[1][i].replace(".\n", '')
                #print(line[1][i])
        returnArr.append(line)
    return returnArr

def countBags(arr, bag):
    numberOfBags = 0
    for line in arr:
        if bag in line[0]:
            for element in line[1]:
                if element[0] != 'n':
                    temp = int(element[0])
                    #print(temp)
                    numberOfBags += temp
                    numberOfBags += temp*countBags(arr, element[2:])
    return numberOfBags



#=====================================================================
inputFile = open("input.txt", 'r')
arr = []
for line in inputFile:
    line = line.split(" contain ")
    arr.append(line)
inputFile.close()
arr = prepareArr(arr)
print(arr)
print(countBags(arr, "shiny gold"))



