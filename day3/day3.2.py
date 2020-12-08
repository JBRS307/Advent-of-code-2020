f = open("input.txt", 'r')
arr = f.read().splitlines()
f.close()
treeCount = 0
index = 0
res = 1
for row in arr:
    if index >= len(row):
        index -= len(row)
    if row[index] == '#':
        treeCount+=1
    index += 1
res *= treeCount
treeCount = 0
index = 0
for row in arr:
    if index >= len(row):
        index -= len(row)
    if row[index] == '#':
        treeCount+=1
    index += 3
res *= treeCount
treeCount = 0
index = 0
for row in arr:
    if index >= len(row):
        index -= len(row)
    if row[index] == '#':
        treeCount+=1
    index += 5
res *= treeCount
treeCount = 0
index = 0
for row in arr:
    if index >= len(row):
        index -= len(row)
    if row[index] == '#':
        treeCount+=1
    index += 7
res *= treeCount
treeCount = 0
index = 0
for i in range(0, len(arr), 2):
    if index >= len(arr[i]):
        index -= len(arr[i])
    if arr[i][index] == '#':
        treeCount+=1
    index += 1
res*=treeCount
print(res)


