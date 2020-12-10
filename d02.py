# Day 2: Password Philosophy
# https://adventofcode.com/2020/day/2

def isCorrect_part1(mn, mx, l, p):
	'''
	Checks if the number of letters l is between mn and mx in password p
	'''
	n = 0
	for e in p:
		if e == l:
			n += 1
	if n >= mn and n <= mx:
		return True
	else:
		return False

def isCorrect_part2(mn, mx, l, p):
	'''
	Checks if the letter l is either in position mn or in position mx in password p
	'''
	if (p[mn-1] == l and p[mx-1] != l) or (p[mn-1] != l and p[mx-1] == l):
		return True
	else:
		return False

def getNbCorrectPasswords(lines, checkFunc):
	'''
	Returns the number of correct passwords according to checkFunc
	'''
	count = 0
	for l in lines:
		a = l.split(':')
		b = a[0].split('-')
		c = b[1].split(' ')
		mn = int(b[0])
		mx = int(c[0])
		l = c[1]
		p = a[1][1:]
		if checkFunc(mn, mx, l, p):
			count += 1
	return count

# main
	
file1 = open('input/input02.txt', 'r')
lines = file1.readlines()

print("Part 1:")
print(getNbCorrectPasswords(lines, isCorrect_part1))

print("Part 2:")
print(getNbCorrectPasswords(lines, isCorrect_part2))

file1.close()
