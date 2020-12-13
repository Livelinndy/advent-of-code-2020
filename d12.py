# Day 12: Rain Risk
# https://adventofcode.com/2020/day/12

import turtle

def part1(lines):
	'''
	Returns the ship's final Manhattan distance from its starting position
	(using part 1 instructions)
	'''
	# the default initial ship position is (0,0) facing east
	# this is also the default initial position of the turtle
	ship = turtle.Turtle() 
	ship.penup()
	for line in lines:
		# current ship position
		x, y = ship.pos()
		# current command
		cmd = line[0]
		n = float(line[1:])
		if cmd == 'N': # move the ship north
			ship.goto(x, y+n)
		elif cmd == 'S': # move the ship south
			ship.goto(x, y-n)
		elif cmd == 'E': # move the ship east
			ship.goto(x+n, y)
		elif cmd == 'W': # move the ship west
			ship.goto(x-n, y)
		elif cmd == 'L': # turn the ship left
			ship.left(n)
		elif cmd == 'R': # turn the ship right
			ship.right(n)
		elif cmd == 'F': # move the ship forward
			ship.forward(n)
	# final ship position
	x, y = ship.pos()
	# Manhattan distance
	d = abs(x) + abs(y)
	return d

def part2(lines):
	'''
	Returns the ship's final Manhattan distance from its starting position
	(using part 2 instructions)
	'''
	# the default initial ship position is (0,0) facing east
	# this is also the default initial position of the turtle
	ship = turtle.Turtle()
	ship.penup()
	# the default initial waypoint position is (10,1)
	waypoint = turtle.Turtle()
	waypoint.penup()
	waypoint.goto(10,1)
	for line in lines:
		# current ship position
		xs, ys = ship.pos()
		# current waypoint position
		xw, yw = waypoint.pos()
		# difference of position between the waypoint and the ship
		dx = xw-xs
		dy = yw-ys
		# current command
		cmd = line[0]
		n = float(line[1:])
		if cmd == 'N': # move the waypoint north
			waypoint.goto(xw, yw+n)
		elif cmd == 'S': # move the waypoint south
			waypoint.goto(xw, yw-n)
		elif cmd == 'E': # move the waypoint east
			waypoint.goto(xw+n, yw)
		elif cmd == 'W': # move the waypoint west
			waypoint.goto(xw-n, yw)
		elif cmd == 'L' or cmd == 'R': # turn the waypoint around the ship
			if cmd == 'L': # left
				waypoint.goto(xs, ys)
				waypoint.left(n)
				waypoint.forward(dx)
				waypoint.left(90)
				waypoint.forward(dy)
				waypoint.right(90)
				waypoint.right(n)
			else: # right
				waypoint.goto(xs, ys)
				waypoint.right(n)
				waypoint.forward(dx)
				waypoint.left(90)
				waypoint.forward(dy)
				waypoint.right(90)
				waypoint.left(n)
		elif cmd == 'F': # move the ship toward the waypoint
			ship.goto(xs+(dx*n), ys+(dy*n))
			waypoint.goto(xw+(dx*n), yw+(dy*n)) # the waypoint moves with the ship
	# final ship position
	xs, ys = ship.pos()
	# Manhattan distance
	d = abs(xs) + abs(ys)
	return d
	
# main
	
file1 = open('input/input12.txt', 'r')
lines = file1.readlines()

print("WARNING: turtle very is slow... but it will get there eventually")

print("Part 1:")
print(part1(lines))

print("Part 2:")
print(part2(lines))

file1.close()