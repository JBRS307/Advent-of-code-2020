def changeDirection(turn, degree, currDirection):
    #turn - left or right, degrees to turn
    change = degree/90
    if turn == 'R':
        currDirection += change
        if currDirection > 3:
            currDirection -= 4
    if turn == 'L':
        currDirection -= change
        if currDirection < 0:
            currDirection += 4
    return currDirection
    

def task1(arr):
    #directions: 0-E, 1-S, 2-W, 3-N
    currDirection = 0 #index of currently faced direction
    NS = 0 #north/south position (north +, south -)
    WE = 0 #west/east position (east +, west -)

    for instr in arr:
        if instr[0] == 'N':
            NS += instr[1]
        elif instr[0] == 'S':
            NS -= instr[1]
        elif instr[0] == 'E':
            WE += instr[1]
        elif instr[0] == 'W':
            WE -= instr[1]
        elif instr[0] == 'F':
            if currDirection == 0:
                WE += instr[1]
            elif currDirection == 1:
                NS -= instr[1]
            elif currDirection == 2:
                WE -= instr[1]
            elif currDirection == 3:
                NS += instr[1]
        elif instr[0] == 'R':
            currDirection = changeDirection('R', instr[1], currDirection)
        elif instr[0] == 'L':
            currDirection = changeDirection('L', instr[1], currDirection)
    return abs(WE) + abs(NS)

#=====================================================================
inputFile = open("input.txt" ,'r')
arr = []
for line in inputFile:
    temp = []
    temp.append(line[0])
    temp.append(int(line[1:]))
    arr.append(temp)
inputFile.close()
print(task1(arr))
