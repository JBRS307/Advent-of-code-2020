f = open("input1.txt", 'r')
arr = f.read().splitlines()
f.close()
for i in range(len(arr)):
    for j in range(i+1, len(arr)):
        if int(arr[j]) + int(arr[i]) == 2020:
            print(int(arr[j])*int(arr[i]))
            break