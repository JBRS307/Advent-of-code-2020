#======================================================================================
inputFile = open("input.txt", 'r')
group = []
arr = []
for line in inputFile:
    line = line[:-1]
    if line != '':
        group.append(line)
    if line == '':
        arr.append(group)
        group = []
        continue
inputFile.close()
#print(arr)

answersSum = 0
for groups in arr:
    yesAnswers = groups[0]
    if len(groups) == 1:
        answersSum += len(yesAnswers)
    else:
        for i in range(1, len(groups)):
            for char in yesAnswers:
                if char not in groups[i]:
                    yesAnswers = yesAnswers.replace(char, '')
        answersSum += len(yesAnswers)
print(answersSum)
