f = open("input.txt", 'r')
arr = f.read().splitlines()
f.close()
treeCount = 0
index = 0
for row in arr:
    if index >= len(row):
        index -= len(row)
    if row[index] == '#':
        treeCount+=1
    index +=3
print(treeCount)