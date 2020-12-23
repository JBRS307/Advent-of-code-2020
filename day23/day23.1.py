def part1(arr):
    i = len(arr)-1 #i - index of the "current" cup
    curr = arr[i] #number of the "current" cup
    for _ in range(100):
        destination = arr[i]-1
        index1, index2, index3 = i-1, i-2, i-3
        cup1, cup2, cup3 = arr[index1], arr[index2], arr[index3]
        arr.remove(cup1)
        arr.remove(cup2)
        arr.remove(cup3)
        while destination not in arr:
            destination -= 1
            if destination < 0:
                destination = max(arr)
        arr.insert(arr.index(destination), cup1)
        arr.insert(arr.index(cup1), cup2)
        arr.insert(arr.index(cup2), cup3)
        i = arr.index(curr)-1
        if i == -1:
            i = len(arr)-1
        curr = arr[i]
    arr = list(reversed(arr[arr.index(1)+1:] + arr[:arr.index(1)]))
    for i in range(len(arr)):
        arr[i] = str(arr[i])
    return ''.join(arr)
    
        

#========================================================
inputFile = open('input.txt', 'r')
arr = list(reversed(inputFile.read()))
for i in range(len(arr)):
    arr[i] = int(arr[i])
inputFile.close()
print(part1(arr))
