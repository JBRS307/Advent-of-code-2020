inputFile = open("input.txt", 'r')
arr = inputFile.readline().split(',')
inputFile.close()
for i in range(len(arr)):
    arr[i] = int(arr[i])
arr.reverse()

for i in range(len(arr), 2020):
    if arr.count(arr[0]) == 1:
        arr.insert(0, 0)
    else:
        arr.insert(0, arr[1:].index(arr[0])+1)
print(arr[0])