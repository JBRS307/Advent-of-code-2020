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
            if arr[i][1][0] == '+':
                arr[i][1] = arr[i][1].replace('+', '')
                acc += int(arr[i][1])
            elif arr[i][1][0] == '-':
                arr[i][1] = arr[i][1].replace('-', '')
                acc -= int(arr[i][1])
            i+=1
            continue
        if arr[i][0] == 'jmp':
            if arr[i][1][0] == '+':
                arr[i][1] = arr[i][1].replace('+', '')
                i += int(arr[i][1])
            elif arr[i][1][0] == '-':
                arr[i][1] = arr[i][1].replace('-', '')
                i -= int(arr[i][1])
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
