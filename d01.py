# Day 1: Report Repair
# https://adventofcode.com/2020/day/1

from itertools import combinations
from functools import reduce
import operator

def part1_naive(lines):
	'''
	Returns the product of 2 numbers which sum is 2020
	'''
	for i in range(len(lines)):
		for j in range(len(lines)):
			if i != j:
				a = int(lines[i])
				b = int(lines[j])
				if a + b == 2020:
					return a * b

def part1_optimized(arr):
	'''
	Returns the product of 2 numbers from arr which sum is 2020
	'''
	arr.sort() # O(n.log(n))
	i=0
	j= len(arr) - 1
	while i != j: # O(n)
		a = arr[i] + arr[j]
		if a == 2020:
			return arr[i] * arr[j] 
		elif a < 2020:
			i += 1
		else:
			j -= 1
		
def part2_naive(lines):
	'''
	Returns the product of 3 numbers from arr which sum is 2020
	'''
	for i in range(len(lines)):
		for j in range(len(lines)):
			for k in range(len(lines)):
				if i != j and i != k and j != k:
					a = int(lines[i])
					b = int(lines[j])
					c = int(lines[k])
					if a + b + c == 2020:
						return a * b * c
						
def both_parts(arr, n):
	'''
	Returns the product of n numbers from arr which sum is 2020
	'''
	for p in combinations(arr, n):
		if sum(p) == 2020:
			return reduce(operator.mul, p)

# main
			
file1 = open('input/input01.txt', 'r') 
lines = file1.readlines()
arr = [int(l) for l in lines]

print("Part 1:")
#print(part1_naive(lines))
print(part1_optimized(arr))
#print(both_parts(arr, 2))

print("Part 2:")
#print(part2_naive(lines))
print(both_parts(arr, 3))

file1.close()