from math import inf

def task1(timestamp, bus):
    nextBus = bus - (timestamp%bus) #minutes until next bus
    return nextBus



#==============================================================================
inputFile = open("input.txt", 'r')
timestamp = int(inputFile.readline())
buses = inputFile.readline().split(',')
inputFile.close()

for i in range(buses.count('x')):
    buses.remove('x')

for i in range(len(buses)):
    buses[i] = int(buses[i])

times = dict()
for bus in buses:
    times[bus] = task1(timestamp, bus)
keyMin = min(times.keys(), key=(lambda k: times[k]))
print(keyMin*times[keyMin])