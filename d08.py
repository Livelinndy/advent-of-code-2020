# Day 8: Handheld Halting
# https://adventofcode.com/2020/day/8

def part1(lines):
	'''
	Returns the value of acc just before the program loops on itself
	'''
	visited = []
	acc = 0
	i = 0
	while i not in visited:
		visited.append(i)
		a = lines[i].split(' ')
		cmd = a[0]
		op = a[1][0]
		n = int(a[1][1:])
		if cmd == "nop":
			i += 1
		elif cmd == "jmp":
			if op == "+": i += n
			elif op == "-": i -= n
		elif cmd == "acc":
			if op == "+": acc += n
			elif op == "-": acc -= n
			i += 1
	return acc

def terminates(lines, nJmpNop):
	'''
	Checks if the program terminates if we replace the nth jmp/nop by the opposite command
	'''
	l = len(lines)
	visited = []
	acc = 0
	i = 0
	nbJmpNop = 0
	while i not in visited:
		if i >= l: return True
		visited.append(i)
		a = lines[i].split(' ')
		cmd = a[0]
		op = a[1][0]
		n = int(a[1][1:])
		if cmd == "nop":
			nbJmpNop += 1
			if nbJmpNop == nJmpNop:
				if op == "+": i += n
				elif op == "-": i -= n
			else:
				i += 1
		elif cmd == "jmp":
			nbJmpNop += 1
			if nbJmpNop == nJmpNop:
				i += 1
			else:
				if op == "+": i += n
				elif op == "-": i -= n
		elif cmd == "acc":
			if op == "+": acc += n
			elif op == "-": acc -= n
			i += 1
	return False
	
def getFinalAcc(lines, nJmpNop):
	'''
	Returns the final value of acc
	(If and only if the replacement of the nth jmp/nop by the opposite command makes the program terminate,
	otherwise returns -1)
	'''
	l = len(lines)
	visited = []
	acc = 0
	i = 0
	nbJmpNop = 0
	while 1:
		if i >= l: return acc
		a = lines[i].split(' ')
		cmd = a[0]
		op = a[1][0]
		n = int(a[1][1:])
		if cmd == "nop":
			nbJmpNop += 1
			if nbJmpNop == nJmpNop:
				if op == "+": i += n
				elif op == "-": i -= n
			else:
				i += 1
		elif cmd == "jmp":
			nbJmpNop += 1
			if nbJmpNop == nJmpNop:
				i += 1
			else:
				if op == "+": i += n
				elif op == "-": i -= n
		elif cmd == "acc":
			if op == "+": acc += n
			elif op == "-": acc -= n
			i += 1
	return -1
	
def part2(lines):
	'''
	Finds the index of the jmp/nop to replace by the opposite command so the program terminates,
	uses this index to calculate the final value of acc,
	returns the final value of acc
	'''
	l = len(lines)
	for i in range(1,l):
		if terminates(lines, i):
			return getFinalAcc(lines, i)
	return -1
	
# main
	
file1 = open('input/input08.txt', 'r')
lines = file1.readlines()

print("Part 1:")
print(part1(lines))

print("Part 2:")
print(part2(lines))
	
file1.close()