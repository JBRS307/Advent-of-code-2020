from copy import deepcopy

def findLoop(arr):
    checked = []
    i = 0
    acc = 0
    while i not in checked:
        if i >= len(arr):
            return acc, True
        checked.append(i)
        if arr[i][0] == 'nop':
            i+=1
            continue
        if arr[i][0] == 'acc':
            acc += int(arr[i][1])
            i+=1
            continue
        if arr[i][0] == 'jmp':
            i += int(arr[i][1])
            continue
    return acc, False

def findError(arr):
    for i in range(len(arr)):
        newArr = deepcopy(arr)
        if newArr[i][0] == 'acc':
            continue
        if newArr[i][0] == 'jmp':
            newArr[i][0] = 'nop'
        elif newArr[i][0] == 'nop':
            newArr[i][0] = 'jmp'
        res, valid = findLoop(newArr)
        if valid == True:
            return res


#===============================================================================
inputFile = open("input.txt", 'r')
arr = []
for line in inputFile:
    line = line.split()
    arr.append(line)
inputFile.close()

print(findError(arr))
