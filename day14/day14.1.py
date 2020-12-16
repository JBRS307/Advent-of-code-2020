def prepareArr(arr):
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if 'mask' in arr[i][j]:
                arr[i][j] = arr[i][j][7:-1]
            else:
                arr[i][j] = arr[i][j].replace('mem[', '')
                arr[i][j] = arr[i][j].replace(']', '')
                arr[i][j] = arr[i][j].replace('\n', '')
    return arr

def task1(arr):
    mem = dict()
    for line in arr:
        for i in range(1, len(line)):
            temp = line[i].split(" = ")
            value = bin(int(temp[1]))
            value = value[2:]
            for j in range(36-len(value)):
                value = '0' + value
            value = list(value)
            for j in range(len(line[0])):
                if line[0][j] == 'X':
                    continue
                value[j] = line[0][j]
            value = "".join(value)
            value = int(value, 2)
            mem[int(temp[0])] = value
    res = 0
    for val in mem.values():
        res += val
    return res


#===========================================================================================
inputFile = open("input.txt", 'r')
arr = []
temp = []
for line in inputFile:
    if 'mask' in line:
        arr.append(temp)
        temp = []
    temp.append(line)
arr.append(temp)
arr.pop(0)
inputFile.close()
arr = prepareArr(arr)
print(task1(arr))