from collections import defaultdict

def getInput(inputFile):
    fields = []
    cond = []
    myTicket = []
    nearbyTickets = []
    for line in inputFile:
        if line == '\n':
            break
        line = line.split(': ')
        fields.append(line[0])
        line = line[1]
        line = line.replace('\n', '')
        line = line.split(' or ')
        temp = []
        for pos in line:
            pos = pos.split('-')
            for i in range(len(pos)):
                pos[i] = int(pos[i])
            temp.append(pos)
        cond.append(temp)
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
    return fields, cond, myTicket, nearbyTickets

def assingNumbers(cond):
    numbers = set()
    for line in cond:
        for interval in line:
            for i in range(interval[0], interval[1]+1):
                numbers.add(i)
    return numbers

def task1(numbers, nearbyTickets):
    i = 0
    while i < len(nearbyTickets):
        for num in nearbyTickets[i]:
            if num not in numbers:
                nearbyTickets.pop(i)
                i-=1
        i+=1
    return nearbyTickets

#------------------------------PART-2-----------------------------------
def makeTable(fields, cond):
    table = defaultdict(set)
    for i, field in enumerate(fields):
        for j in range(len(cond[i])):
            for k in range(cond[i][j][0], cond[i][j][1]+1):
                table[field].add(k)
    return table

def clearColumns(columns, fields, removedSet):
    for i in range(len(fields)):
        if len(columns[i]) == 1 and columns[i][0] not in removedSet:
            removed = columns[i][0]
            removedSet.add(removed)
            break
    
    for i in range(len(fields)):
        if len(columns[i]) > 1:
            try:
                columns[i].remove(removed)
            except:
                continue
    
    for i in range(len(fields)):
        if len(columns[i]) > 1:
            return clearColumns(columns, fields, removedSet)
    return columns
        


def task2(table, nearbyTickets, fields):
    columns = defaultdict(list)
    for i in range(len(nearbyTickets[0])):
        for field in fields:
            for ticket in nearbyTickets:
                if ticket[i] not in table[field]:
                    break
            else:
                columns[i].append(field)
    
    columns = clearColumns(columns, fields, set())

    indexSet = set()
    for i in range(len(columns)):
        if 'departure' in columns[i][0]:
            indexSet.add(i)
    
    res = 1
    myTicket = nearbyTickets[-1]
    for index in indexSet:
        res *= myTicket[index]
    return res
#=========================================================================
inputFile = open("input.txt", 'r')
fields, cond, myTicket, nearbyTickets = getInput(inputFile)
inputFile.close()
numbers = assingNumbers(cond)
#print(numbers)
nearbyTickets = task1(numbers, nearbyTickets)
nearbyTickets.append(myTicket)
table = makeTable(fields, cond)
#print(table)
#print(cond)
#print(nearbyTickets)
#print(fields)
print(task2(table, nearbyTickets, fields))


