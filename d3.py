# Day 3: Toboggan Trajectory
# https://adventofcode.com/2020/day/3

from functools import reduce
import operator

def getTrees(right, down):
	trees = 0
	i = right
	j = down
	while j <= m:
		k = i
		if i >= n:
			k %= n
		if lines[j][k] == '#':
			trees += 1
		i += right
		j += down
	return trees

# main
	
file1 = open('input/input3.txt', 'r')
lines = file1.readlines()
n = len(lines[0]) - 1
m = len(lines) - 1

print("Part 1:")
print(getTrees(3,1))

print("Part 2:")
res = [getTrees(1,1), getTrees(3,1), getTrees(5,1), getTrees(7,1), getTrees(1,2)]
print(reduce(operator.mul, res))

file1.close()