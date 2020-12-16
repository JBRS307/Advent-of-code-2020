def part2(buses):
    mods = {}
    for idx, bus in enumerate(buses):
        if bus != 'x':
            mods[bus] = -idx % bus
    print(mods)

    iterator = 0
    increment = 1
    for bus in mods.keys():
        while iterator % bus != mods[bus]:
            iterator += increment
        increment *= bus

    return iterator



#====================================================================
inputFile = open("test.txt", 'r')
timestamp = int(inputFile.readline())
buses = inputFile.readline().split(',')
inputFile.close()

for i in range(len(buses)):
    if buses[i].isdigit():
        buses[i] = int(buses[i])

print(part2(buses))