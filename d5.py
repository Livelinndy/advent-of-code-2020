# Day 5: Binary Boarding
# https://adventofcode.com/2020/day/5

def getSeatIds(lines):
	lst = []
	for l in lines:
		cs = { "mn": 0, "mx": 127 }
		c = 0
		for i in range(0,6):
			if l[i] == "F": cs["mx"] = int((cs["mn"]+cs["mx"])/2)
			else: cs["mn"] = int((cs["mn"]+cs["mx"])/2) + 1
		if l[6] == "F": c = cs["mn"]
		else: c = cs["mx"]
		rs = { "mn": 0, "mx": 7 }
		r = 0
		for j in range(7,9):
			if l[j] == "L": rs["mx"] = int((rs["mn"]+rs["mx"])/2)
			else: rs["mn"] = int((rs["mn"]+rs["mx"])/2) + 1
		if l[9] == "L": r = rs["mn"]
		else: r = rs["mx"]
		id = (c * 8) + r
		lst.append(id)
	lst.sort()
	return lst

def getMaxSeatId(lst):
	return lst[-1]

def getMySeatId(lst):
	prev = 0
	for id in lst:
		if id == prev + 2:
			return prev + 1
		prev = id
	return -1
	
# main
	
file1 = open('input/input5.txt', 'r')
lines = file1.readlines()

lst = getSeatIds(lines)

print("Part 1:")
print(getMaxSeatId(lst))

print("Part 2:")
print(getMySeatId(lst))

file1.close()
