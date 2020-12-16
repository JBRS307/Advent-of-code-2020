res = set()

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

def findMems(index, positionX):
    if len(positionX) <= 0:
        return
    global res
    res.add(index)
    findMems(index, positionX[1:])
    index = list(index)
    index[positionX[0]] = '1'
    index = "".join(index)
    res.add(index)
    findMems(index, positionX[1:])

    
        
    

def task2(arr):
    global res
    mem = dict()
    for line in arr:
        for i in range(1, len(line)):
            temp = line[i].split(" = ")
            value = bin(int(temp[0]))
            value = value[2:]
            for j in range(36-len(value)):
                value = '0' + value
            value = list(value)
            for j in range(len(line[0])):
                if line[0][j] == '0':
                    continue
                elif line[0][j] == '1':
                    value[j] = '1'
                else:
                    value[j] = 'X'
            res.clear()
            positionX = []
            for j in range(len(value)-1, -1, -1):
                if value[j] == 'X':
                    positionX.append(j)
                    value[j] = '0'
            value = "".join(value)
            findMems(value, positionX)
            for index in res:
                mem[int(index, 2)] = int(temp[1])
            #print(mem)
    result = 0
    for val in mem.values():
        result += val
    return result


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
#print(arr)
print(task2(arr))