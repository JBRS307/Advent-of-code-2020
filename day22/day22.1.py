def getInput(inputFile):
    inputFile.readline()
    player1 = []
    player2 = []
    for line in inputFile:
        if line == '\n':
            break
        player1.append(int(line[:-1]))
    inputFile.readline()
    for line in inputFile:
        player2.append(int(line[:-1]))
    return player1, player2

def part1(player1, player2):
    while len(player1) > 0 and len(player2) > 0:
        card1 = player1.pop(0)
        card2 = player2.pop(0)
        if card1 > card2:
            player1.append(card1)
            player1.append(card2)
        elif card1 < card2:
            player2.append(card2)
            player2.append(card1)
    if len(player1) > len(player2):
        res = 0
        for i in range(-1, -len(player1)-1, -1):
            res += player1[i]*(-i)
        return res
    else:
        res = 0
        for i in range(-1, -len(player2)-1, -1):
            res += player2[i]*(-i)
        return res
#================================================
inputFile = open('input.txt', 'r')
player1, player2 = getInput(inputFile)
inputFile.close()

print(f"Part 1: {part1(player1, player2)}")

