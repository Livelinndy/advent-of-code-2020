# Day 11: Seating System
# https://adventofcode.com/2020/day/11

def printSeats(seats):
	for row in seats:
		line = ""
		for seat in row:
			line += seat[-1]
		print(line)

# simple checks

def isOccupied(seats, r, c, round):
	if seats[r][c][round] == '#':
		return True
	return False

def isFree(seats, r, c, round):
	if seats[r][c][round] == 'L':
		return True
	return False	

# looking left
		
def checkLeft_part1(seats, r, c, round):
	if c == 0:
		return 0
	return isOccupied(seats, r, c-1, round)

def checkLeft_part2(seats, r, c, round):
	if c == 0:
		return 0
	i = c-1
	while i>=0:
		if isFree(seats, r, i, round):
			return 0
		elif isOccupied(seats, r, i, round):
			return 1
		i -= 1
	return 0
		
# looking right
		
def checkRight_part1(seats, r, c, round):
	if c == nbColumns-1:
		return 0
	return isOccupied(seats, r, c+1, round)
	
def checkRight_part2(seats, r, c, round):
	if c == nbColumns-1:
		return 0
	i = c+1
	while i<nbColumns:
		if isFree(seats, r, i, round):
			return 0
		elif isOccupied(seats, r, i, round):
			return 1	
		i += 1
	return 0
		
# looking up
		
def checkUp_part1(seats, r, c, round):
	if r == 0:
		return 0
	return isOccupied(seats, r-1, c, round)

def checkUp_part2(seats, r, c, round):
	if r == 0:
		return 0
	j = r-1
	while j>=0:
		if isFree(seats, j, c, round):
			return 0
		elif isOccupied(seats, j, c, round):
			return 1	
		j -= 1
	return 0
		
# looking down
		
def checkDown_part1(seats, r, c, round):
	if r == nbRows-1:
		return 0
	return isOccupied(seats, r+1, c, round)

def checkDown_part2(seats, r, c, round):
	if r == nbRows-1:
		return 0
	j = r+1
	while j<nbRows:
		if isFree(seats, j, c, round):
			return 0
		elif isOccupied(seats, j, c, round):
			return 1	
		j += 1
	return 0
		
# looking up left
		
def checkUpLeft_part1(seats, r, c, round):
	if c == 0 or r == 0:
		return 0
	return isOccupied(seats, r-1, c-1, round)	

def checkUpLeft_part2(seats, r, c, round):
	if c == 0 or r == 0:
		return 0
	i = c-1
	j = r-1
	while i>=0 and j>=0:
		if isFree(seats, j, i, round):
			return 0
		elif isOccupied(seats, j, i, round):
			return 1	
		i -= 1
		j -= 1
	return 0
		
# looking up right	
	
def checkUpRight_part1(seats, r, c, round):
	if c == nbColumns-1 or r == 0:
		return 0
	return isOccupied(seats, r-1, c+1, round)

def checkUpRight_part2(seats, r, c, round):
	if c == nbColumns-1 or r == 0:
		return 0
	i = c+1
	j = r-1
	while i<nbColumns and j>=0:
		if isFree(seats, j, i, round):
			return 0
		elif isOccupied(seats, j, i, round):
			return 1	
		i += 1
		j -= 1
	return 0
		
# looking down left
		
def checkDownLeft_part1(seats, r, c, round):
	if c == 0 or r == nbRows-1:
		return 0
	return isOccupied(seats, r+1, c-1, round)

def checkDownLeft_part2(seats, r, c, round):
	if c == 0 or r == nbRows-1:
		return 0
	i = c-1
	j = r+1
	while i>=0 and j<nbRows:
		if isFree(seats, j, i, round):
			return 0
		elif isOccupied(seats, j, i, round):
			return 1	
		i -= 1
		j += 1
	return 0
		
# looking down right
		
def checkDownRight_part1(seats, r, c, round):
	if c == nbColumns-1 or r == nbRows-1:
		return 0
	return isOccupied(seats, r+1, c+1, round)	

def checkDownRight_part2(seats, r, c, round):
	if c == nbColumns-1 or r == nbRows-1:
		return 0
	i = c+1
	j = r+1
	while i<nbColumns and j<nbRows:
		if isFree(seats, j, i, round):
			return 0
		elif isOccupied(seats, j, i, round):
			return 1
		i += 1
		j += 1
	return 0
		
# getting the number of occupied seats
		
def getNbOccupiedSeatsAround_part1(seats, r, c, round):
	n = checkLeft_part1(seats, r, c, round)
	n += checkRight_part1(seats, r, c, round)
	n += checkUp_part1(seats, r, c, round)
	n += checkDown_part1(seats, r, c, round)
	n += checkUpLeft_part1(seats, r, c, round)
	n += checkUpRight_part1(seats, r, c, round)
	n += checkDownLeft_part1(seats, r, c, round)
	n += checkDownRight_part1(seats, r, c, round)
	return n
	
def getNbOccupiedSeatsAround_part2(seats, r, c, round):
	n = checkLeft_part2(seats, r, c, round)
	n += checkRight_part2(seats, r, c, round)
	n += checkUp_part2(seats, r, c, round)
	n += checkDown_part2(seats, r, c, round)
	n += checkUpLeft_part2(seats, r, c, round)
	n += checkUpRight_part2(seats, r, c, round)
	n += checkDownLeft_part2(seats, r, c, round)
	n += checkDownRight_part2(seats, r, c, round)
	return n

def getTotalNbOccupiedSeats(seats, round):
	n = 0
	for row in seats:
		for seat in row:
			if seat[round] == '#':
				n += 1
	return n
	
# simulation
	
def simulate(seats, getNbOccupiedSeatsAroundFunc, tolerance):
	'''
	Simulates seat occupation and returns the final number of occupied seats
	'''
	prevOccupied = -1
	round = 0
	while 1:
		#print("Round " + str(round))
		#printSeats(seats)
		for r in range(0, nbRows):
			for c in range(0, nbColumns):
				s = seats[r][c][-1]
				if s == 'L' or s == '#':
					n = getNbOccupiedSeatsAroundFunc(seats, r, c, round)
					if s == 'L':
						if n == 0:
							seats[r][c] += "#"
						else:
							seats[r][c] += "L"
					else:
						if n >= tolerance:
							seats[r][c] += "L"
						else:
							seats[r][c] += "#"
				else:
					seats[r][c] += "."
		round += 1
		currOccupied = getTotalNbOccupiedSeats(seats, round)
		if currOccupied == prevOccupied:
			break
		prevOccupied = currOccupied
	return prevOccupied
	
# main
	
file1 = open('input/input11.txt', 'r')
lines = file1.readlines()

nbRows = len(lines)
nbColumns = len(lines[0])-1 # not counting the newline character

seats = []
for r in range(0, nbRows):
	row = []
	for c in range(0, nbColumns):
		row.append(lines[r][c])
	seats.append(row)

print("Part 1:")		
print(simulate(seats, getNbOccupiedSeatsAround_part1, 4))

for r in range(0, nbRows):
	for c in range(0, nbColumns):
		s = seats[r][c][-1]
		if s == 'L' or s == '#':
			seats[r][c] = 'L'
		else:
			seats[r][c] = '.'

print("Part 2:")
print(simulate(seats, getNbOccupiedSeatsAround_part2, 5))

file1.close()