def task1(arr):
    newArr = arr[:]
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if arr[i][j] == '.':
                continue
            check = ""
            if i > 0 and j > 0:
                check += arr[i-1][j-1]
            if i > 0:
                check += arr[i-1][j]
            if i > 0 and j < (len(arr[i])-1):
                check += arr[i-1][j+1]
            if j < (len(arr[i])-1):
                check += arr[i][j+1]
            if i < (len(arr)-1) and j < (len(arr[i])-1):
                check += arr[i+1][j+1]
            if i < (len(arr)-1):
                check += arr[i+1][j]
            if i < (len(arr)-1) and j > 0:
                check += arr[i+1][j-1]
            if j > 0:
                check += arr[i][j-1]
            
            check = sorted(check)
            if '#' not in check and arr[i][j] == 'L':
                if j == 0:
                    newArr[i] = '#' + newArr[i][1:]
                elif j == len(arr[i]) - 1:
                    newArr[i] = newArr[i][:-1] + '#'
                else:
                    newArr[i] = newArr[i][:j] + '#' + newArr[i][j+1:]
            if check.count('#') >= 4 and arr[i][j] == '#':
                if j == 0:
                    newArr[i] = 'L' + newArr[i][1:]
                elif j == len(arr[i])-1:
                    newArr[i] = newArr[i][:-1] + 'L'
                else:
                    newArr[i] = newArr[i][:j] + 'L' + newArr[i][j+1:]
    if arr != newArr:
        return task1(newArr)

    res = 0
    for line in arr:
        res += line.count('#')
    return res
            
#=========================================================================
inputFile = open("input.txt", 'r')
arr = inputFile.read().splitlines()
inputFile.close()
print(task1(arr))

#spaghetti as fuck, but works


