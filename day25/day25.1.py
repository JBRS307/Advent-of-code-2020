def getLoopSize(key):
    value = 1
    loopSize = 0
    while value != key:
        value *= 7
        value = value%20201227
        loopSize+=1
    return loopSize

def makeEncryptionKey(key, loopSize):
    value = 1
    for _ in range(loopSize):
        value *= key
        value = value%20201227
    return value


#===========================================================================
inputFile = open('input.txt', 'r')
cardKey, doorKey = inputFile.read().splitlines()
cardKey, doorKey = int(cardKey), int(doorKey)
inputFile.close()


print(f"Part 1: {makeEncryptionKey(doorKey, getLoopSize(cardKey))}")



