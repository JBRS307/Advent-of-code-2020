def getInput(inputFile):
    cond = []
    myTicket = []
    nearbyTickets = []
    for line in inputFile:
        if line == '\n':
            break
        line = line.split(': ')
        line = line[1]
        line = line.replace('\n', '')
        line = line.split(' or ')
        for pos in line:
            pos = pos.split('-')
            for i in range(len(pos)):
                pos[i] = int(pos[i])
            cond.append(pos)
    inputFile.readline()
    myTicket = inputFile.readline().split(',')
    for i in range(len(myTicket)):
        myTicket[i] = int(myTicket[i])
    inputFile.readline()
    inputFile.readline()
    for line in inputFile:
        line = line.split(',')
        for i in range(len(line)):
            line[i] = int(line[i])
        nearbyTickets.append(line)
    return cond, myTicket, nearbyTickets

def asingNumbers(cond):
    numbers = set()
    for interval in cond:
        for i in range(interval[0], interval[1]+1):
            numbers.add(i)
    return numbers

def task1(numbers, nearbyTickets):
    res = 0
    for ticket in nearbyTickets:
        for num in ticket:
            if num not in numbers:
                res += num
    return res

#=========================================================================
inputFile = open("input.txt", 'r')
cond, myTicket, nearbyTickets = getInput(inputFile)
inputFile.close()

numbers = asingNumbers(cond)
print(task1(numbers, nearbyTickets))

