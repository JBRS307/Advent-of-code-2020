from math import ceil

def findRow(seat, start, end):
    if start == end:
        return start
    if seat[0] == 'F':
        return findRow(seat[1:], start, (end-start)//2+start)
    if seat[0] == 'B':
        return findRow(seat[1:], ceil((end-start)/2)+start, end)

def findColumn(seat, start, end):
    if start == end:
        return start
    if seat[0] == 'L':
        return findColumn(seat[1:], start, (end-start)//2+start)
    if seat[0] == 'R':
        return findColumn(seat[1:], ceil((end-start)/2)+start, end)

def part2(arr):
    seatSet = set()
    for seat in arr:
        row, col, = findRow(seat, 0, 127), findColumn(seat[7:], 0, 7)
        seatID = row * 8 + col
        seatSet.add(seatID)
    for i in range(min(seatSet), max(seatSet)):
        if i not in seatSet:
            return i
    return None
#============================================================================================================
inputFile = open("input.txt", 'r')
arr = inputFile.read().splitlines()
inputFile.close()
print(part2(arr))

