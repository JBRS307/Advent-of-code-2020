def changeDirection(turn, degree, wWE, wNS):
    #turn - left or right, degrees to turn
    change = degree//90
    if turn == 'R':
        for i in range(change):
            tempWNS = -wWE
            tempWWE = wNS
            wWE, wNS = tempWWE, tempWNS
    if turn == 'L':
        for i in range(change):
            tempWNS = wWE
            tempWWE = -wNS
            wWE, wNS = tempWWE, tempWNS
    return wNS, wWE
    
    

def task2(arr):
    NS = 0 #north/south position (north +, south -)
    WE = 0 #west/east position (east +, west -)
    wNS = 1 #north/sputh waypoint position
    wWE = 10 #west/east waypoint position

    for instr in arr:
        if instr[0] == 'N':
            wNS += instr[1]
        elif instr[0] == 'S':
            wNS -= instr[1]
        elif instr[0] == 'E':
            wWE += instr[1]
        elif instr[0] == 'W':
            wWE -= instr[1]
        elif instr[0] == 'F':
            NS += wNS*instr[1]
            WE += wWE*instr[1]
        elif instr[0] == 'R':
            wNS, wWE = changeDirection('R', instr[1], wWE, wNS)
        elif instr[0] == 'L':
            wNS, wWE = changeDirection('L', instr[1], wWE, wNS)
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
print(task2(arr))
