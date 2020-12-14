def task1(arr):
    numberOf1 = 0
    numberOf3 = 0

    if arr[0] == 1:
        numberOf1 += 1
    elif arr[0] == 3:
        numberOf3 += 1
    for i in range(1, len(arr)):
        temp = arr[i] - arr[i-1]
        if temp == 1:
            numberOf1 += 1
        elif temp == 3:
            numberOf3 += 1
    return numberOf1*numberOf3

#===============================================================================
inputFile = open("input.txt", 'r')
arr = []
for line in inputFile:
    arr.append(int(line))
inputFile.close()
arr.sort()
arr.append(arr[-1]+3)
print(task1(arr))

