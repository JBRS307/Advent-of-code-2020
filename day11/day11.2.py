def checkVisibleSeats(arr, x, y):
    i, j = x, y
    visibleSeats = []
    
    #top left corner
    while i > 0 and j > 0:
        i-=1
        j-=1
        if arr[i][j] == 'L' or arr[i][j] == '#':
            visibleSeats.append(arr[i][j])
            break
    
    #top right corner
    i, j = x, y
    while i > 0 and j < len(arr[i])-1:
        i-=1
        j+=1
        if arr[i][j] == 'L' or arr[i][j] == '#':
            visibleSeats.append(arr[i][j])
            break
    
    #bottom right corner
    i, j = x, y
    while i < len(arr)-1 and j < len(arr[i])-1:
        i+=1
        j+=1
        if arr[i][j] == 'L' or arr[i][j] == '#':
            visibleSeats.append(arr[i][j])
            break
    
    #bottom left corner
    i, j = x, y
    while i < len(arr)-1 and j > 0:
        i+=1
        j-=1
        if arr[i][j] == 'L' or arr[i][j] == '#':
            visibleSeats.append(arr[i][j])
            break
    
    #top
    i, j = x, y
    while i > 0:
        i-=1
        if arr[i][j] == 'L' or arr[i][j] == '#':
            visibleSeats.append(arr[i][j])
            break
    
    #right
    i, j = x, y
    while j < len(arr[i])-1:
        j+=1
        if arr[i][j] == 'L' or arr[i][j] == '#':
            visibleSeats.append(arr[i][j])
            break
    
    #bottom
    i, j = x, y
    while i < len(arr)-1:
        i+=1
        if arr[i][j] == 'L' or arr[i][j] == '#':
            visibleSeats.append(arr[i][j])
            break
    
    #left
    i, j = x, y
    while j > 0:
        j-=1
        if arr[i][j] == 'L' or arr[i][j] == '#':
            visibleSeats.append(arr[i][j])
            break
    
    return visibleSeats

def task2(arr):
    newArr = arr[:]
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if arr[i][j] == '.':
                continue
            check = checkVisibleSeats(arr, i, j)
            
            if '#' not in check and arr[i][j] == 'L':
                if j == 0:
                    newArr[i] = '#' + newArr[i][1:]
                elif j == len(arr[i])-1:
                    newArr[i] = newArr[i][:-1] + '#'
                else:
                    newArr[i] = newArr[i][:j] + '#' + newArr[i][j+1:]
            if check.count('#') >= 5 and arr[i][j] == '#':
                if j == 0:
                    newArr[i] = 'L' + newArr[i][1:]
                elif j == len(arr[i])-1:
                    newArr[i] = newArr[i][:-1] + 'L'
                else:
                    newArr[i] = newArr[i][:j] + 'L' + newArr[i][j+1:]
    
    if arr != newArr:
        return task2(newArr)
    
    res = 0
    for line in arr:
        res += line.count('#')
    return res

#=========================================================================
inputFile = open("input.txt", 'r')
arr = inputFile.read().splitlines()
inputFile.close()
print(task2(arr))

#still spaghetti, still works
