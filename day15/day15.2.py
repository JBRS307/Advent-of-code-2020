from collections import *

inputFile = open("input.txt", 'r')
arr = inputFile.readline().split(',')
inputFile.close()
for i in range(len(arr)):
    arr[i] = int(arr[i])
turns = 30_000_000

numToSpeak = arr[-1]
turnNum = defaultdict(deque)

for v, k in enumerate(arr):
    turnNum[k].append(v+1)

turn = len(arr)+1
while turn <= turns:
    l = len(turnNum[numToSpeak])

    if l > 1:
        numToSpeak = turnNum[numToSpeak][-1] - turnNum[numToSpeak][-2]
        turnNum[numToSpeak].append(turn)
    else:
        numToSpeak = 0
        turnNum[numToSpeak].append(turn)
    turn+=1
print(numToSpeak)