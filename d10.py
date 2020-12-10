# Day 10: Adapter Array
# https://adventofcode.com/2020/day/10

def part1(arr):
	'''
	Returns the number of 1-jolt differences multiplied by the number of 3-jolt differences
	'''
	n1 = 0
	n2 = 0
	n3 = 0
	prev = 0
	l = len(arr)
	for i in range(0,l):
		if arr[i] - prev == 1:
			n1 += 1
		elif arr[i] - prev == 2:
			n2 += 1
		elif arr[i] - prev == 3:
			n3 += 1
		else:
			return -1
		prev = arr[i]
	n3 += 1
	return n1 * n3
	
def part2(arr):
	'''
	Returns the number of different ways to arrange the adapters
	'''
	l = len(arr)
	ways = [0] * l
	ways[0] = 1
	for i in range(0, l):
		n = ways[i]
		for j in range(i + 1, l):
			if arr[j] - arr[i] > 3:
				break
			ways[j] += n
	return ways[-1]

# main
	
file1 = open('input/input10.txt', 'r')
lines = file1.readlines()

arr = [int(l) for l in lines]
arr.sort()

print("Part 1:")
print(part1(arr))

print("Part 2:")
print(part2([0] + arr))
	
file1.close()