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

def recursiveCombat(player1, player2):
    playedGames = set()
    while len(player1) > 0 and len(player2) > 0:
        if (tuple(player1), tuple(player2)) in playedGames:
            return True

        playedGames.add((tuple(player1), tuple(player2)))
        card1, card2 = player1.pop(0), player2.pop(0)
        if len(player1) >= card1 and len(player2) >= card2:
            if recursiveCombat(player1[:card1], player2[:card2]):
                player1.extend([card1, card2])
            else:
                player2.extend([card2, card1])
        else:
            if card1 > card2:
                player1.extend([card1, card2])
            elif card1 < card2:
                player2.extend([card2, card1])
    if len(player1) > len(player2):
        return True
    else:
        return False


def part2(player1, player2):
    playedGames = set()
    while len(player1) > 0 and len(player2) > 0:
        if (tuple(player1), tuple(player2)) in playedGames:
            res = 0
            for i in range(-1, -len(player1)-1, -1):
                res += player1[i]*(-i)
            return res

        playedGames.add((tuple(player1), tuple(player2)))
        card1, card2 = player1.pop(0), player2.pop(0)
        if len(player1) >= card1 and len(player2) >= card2:
            if recursiveCombat(player1[:card1], player2[:card2]):
                player1.extend([card1, card2])
            else:
                player2.extend([card2, card1])
        else:
            if card1 > card2:
                player1.extend([card1, card2])
            elif card1 < card2:
                player2.extend([card2, card1])
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

print(f"Part 2: {part2(player1, player2)}")

#unoptimized AF, but works