checked = []

def findPossibleBags(arr, bag):
    global checked
    valid = 0
    for rules in arr:
        if bag in rules[1]:
            if rules[0] not in checked:
                checked.append(rules[0])
                valid += 1
                valid += findPossibleBags(arr, rules[0][:-5])
    return valid


#=====================================================================
inputFile = open("input.txt", 'r')
arr = []
for line in inputFile:
    line = line.split(" contain")
    arr.append(line)
inputFile.close()
print(findPossibleBags(arr, "shiny gold"))

