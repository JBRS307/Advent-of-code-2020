def part1(data):
    count = 0
    requiredFields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
    
    current = 0
    for line in data:
        if line == '':
            if current == len(requiredFields):
                count += 1
            current = 0
            continue

        for field in line.split():
            key, val = field.split(':')
            if key in requiredFields:
                current += 1
    return count

#==========================================================================================================
inputfile = open("input.txt", 'r')
data = [x.strip() for x in inputfile]
print(part1(data))
inputfile.close()


