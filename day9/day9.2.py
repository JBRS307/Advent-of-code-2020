def task1(arr):
    for i in range(25):
        for j in range(i+1, 25):
            if int(arr[j]) + int(arr[i]) == int(arr[25]):
                return task1(arr[1:])
    return int(arr[25])

def task2(arr):
    searched = task1(arr)
    for i in range(len(arr)):
        num = int(arr[i])
        for j in range(i+1, len(arr)):
            num+=int(arr[j])
            if num == searched:
                return int(min(arr[i:j+1])) + int(max(arr[i:j+1]))

#===============================================================================================
inputFile = open("input.txt", 'r')
arr = inputFile.read().splitlines()
inputFile.close()
print(task2(arr))