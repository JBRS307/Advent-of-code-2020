inputFile = open("input.txt", 'r')
arr = []
for line in inputFile:
    arr.append(int(line))
inputFile.close()
arr.sort()
arr.append(arr[-1]+3)
print(arr)

sol = {0:1}
for line in arr:
    sol[line] = 0
    if line - 1 in sol:
        sol[line] += sol[line-1]
    if line - 2 in sol:
        sol[line] += sol[line-2]
    if line - 3 in sol:
        sol[line] += sol[line-3]
print(sol[arr[-1]])

#solution stolen


