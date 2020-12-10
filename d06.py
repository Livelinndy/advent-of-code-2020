# Day 6: Custom Customs
# https://adventofcode.com/2020/day/6

from functools import reduce
import operator

def part1(lines):
	'''
	Returns the sum of number of questions that have positive answers from any member in each group
	'''
	answers = ""
	counts = []
	for line in lines:
		if line == "\n":
			answers = ''.join(set(answers))
			counts.append(len(answers))
			answers = ""
		else:
			answers += line.strip()
	answers = ''.join(set(answers))
	counts.append(len(answers))
	res = reduce(operator.add, counts)
	return res

def part2(lines):
	'''
	Returns the sum of number of questions that have positive answers from every member in each group
	'''
	answers = lines[0].strip()
	counts = []
	i = 1
	while i < len(lines):
		if lines[i] == "\n":
			counts.append(len(answers))
			answers = lines[i+1].strip()
			i += 2
		else:
			answers = ''.join(set(answers)&set(lines[i].strip()))
			i += 1
	counts.append(len(answers))
	res = reduce(operator.add, counts)
	return res
	
# main
	
file1 = open('input/input06.txt', 'r')
lines = file1.readlines()

print("Part 1:")
print(part1(lines))

print("Part 2:")
print(part2(lines))

file1.close()