f = open("input1.txt", 'r')
arr = f.read().splitlines()
f.close()
for i in range(len(arr)):
    for j in range(i+1, len(arr)):
        for k in range(j+1, len(arr)):
            if int(arr[i]) + int(arr[j]) + int(arr[k]) == 2020:
                print(int(arr[i])*int(arr[j])*int(arr[k]))
                break