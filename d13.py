# Day 13: Shuttle Search
# https://adventofcode.com/2020/day/13

import math

def part1(lines):
	'''
	Returns the minimal convenient bus departure time multiplied by the number of minutes to wait
	'''
	myDepartureTime = int(lines[0])
	busses = lines[1].split(',')
	busIds = [int(b) for b in busses if b != 'x']
	busDepartureTime = []
	for id in busIds:
		t = math.ceil(myDepartureTime/id) * id
		busDepartureTime.append(t)
	minBusDepartureTime = min(busDepartureTime)
	minsToWait = minBusDepartureTime - myDepartureTime
	res = busIds[busDepartureTime.index(minBusDepartureTime)] * minsToWait
	return res

def part2_version1(lines):
	'''
	Returns the earliest timestamp such that all of the listed bus ids depart at offsets matching their positions in the list
	'''
	busses = lines[1].split(',')
	busIds = [(int(b), busses.index(b)) for b in busses if b != 'x']
	timestamp = 0
	cumulated = 1
	for b in busIds:
		while (timestamp+b[1])%b[0] != 0:
			timestamp += cumulated
		cumulated *= b[0]
	return timestamp

def algoEuclide(a, b):
	'''
	https://fr.wikipedia.org/wiki/Algorithme_d%27Euclide_%C3%A9tendu
	'''
	r, u, v, rbis, ubis, vbis = a, 1, 0, b, 0, 1
	while rbis != 0:
		q = int(r/rbis)
		r, u, v, rbis, ubis, vbis = rbis, ubis, vbis, r-(q*rbis), u-(q*ubis), v-(q*vbis)
	return r, u, v
	
def part2_version2(lines):
	'''
	Returns the earliest timestamp such that all of the listed bus ids depart at offsets matching their positions in the list
	using Euclide's algorithm
	'''
	#l'idée de l'algo d'euclide c'est de trouver rapidement u et v, tel que a.u+b.v=1 du coup, si on veut être égal à i modulo a et j modulo b il suffit d'être égal à i+(j-i)*a.u modulo (a.b)
	pass
		
# main
	
file1 = open('input/input13.txt', 'r')
lines = file1.readlines()

print("Part 1:")
print(part1(lines))

print("Part 2:")
print(part2_version1(lines))

file1.close()