f = open("input.txt", 'r')
arr = []
for i in range(1000):
    a = list(map(str, f.readline().split()))
    arr.append(a)
f.close()
count = 0
for i in arr:
    if len(i[0]) == 3:
        first = int(i[0][0])-1
        second = int(i[0][2])-1
    elif len(i[0]) == 4:
        first = int(i[0][0])-1
        second = int(i[0][2])*10+int(i[0][3])-1
    elif len(i[0]) == 5:
        first = int(i[0][0])*10+int(i[0][1])-1
        second = int(i[0][3])*10+int(i[0][4])-1
    condition = i[1][0]
    if i[2][first] == condition and i[2][second] != condition:
        count+=1
    elif i[2][second] == condition and i[2][first] != condition:
        count+=1
print(count)