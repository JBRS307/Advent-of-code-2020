f = open("input.txt", 'r')
arr = []
for i in range(1000):
    a = list(map(str, f.readline().split()))
    arr.append(a)
f.close()
count = 0
for i in arr:
    if len(i[0]) == 3:
        minimum = int(i[0][0])
        maximum = int(i[0][2])
    elif len(i[0]) == 4:
        minimum = int(i[0][0])
        maximum = int(i[0][2])*10+int(i[0][3])
    elif len(i[0]) == 5:
        minimum = int(i[0][0])*10+int(i[0][1])
        maximum = int(i[0][3])*10+int(i[0][4])
    condition = i[1][0]
    check = i[2].count(condition)
    if check >= minimum and check <= maximum:
        count+=1
print(count)