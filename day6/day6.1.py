inputFile = open("input.txt", 'r')
group = ""
arr = []
for line in inputFile:
    line = line[:-1]
    group += line
    if line == '':
        arr.append(group)
        group = ""
        continue
inputFile.close()

answersSum = 0
for answers in arr:
    answersYes = 0
    for i in range(97, 123):
        char = chr(i)
        if char in answers:
            answersYes+=1
    answersSum += answersYes
print(answersSum)