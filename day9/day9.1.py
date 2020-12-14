def task1(arr):
    for i in range(25):
        for j in range(i+1, 25):
            #temp = arr[i]+arr[j]
            if int(arr[j]) + int(arr[i]) == int(arr[25]):
                return task1(arr[1:])
    return arr[25]

#===============================================================================================
inputFile = open("input.txt", 'r')
arr = inputFile.read().splitlines()
inputFile.close()
print(task1(arr))