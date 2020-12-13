def findLoop(arr):
    checked = []
    i = 0
    acc = 0
    while i not in checked:
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
    return acc

#===============================================================================
inputFile = open("input.txt", 'r')
arr = []
for line in inputFile:
    line = line.split()
    arr.append(line)
inputFile.close()

print(findLoop(arr))
