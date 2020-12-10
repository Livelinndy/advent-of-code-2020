# Day 9: Encoding Error
# https://adventofcode.com/2020/day/9

from itertools import combinations

def isSum(s, arr, n):
	'''
	Checks if s is sum of n numbers in arr
	'''
	for c in combinations(arr, n):
		if sum(c) == s:
			return True
	return False

def getInconvenientValue(arr, p, n):
	'''
	Returns the first number that's not the sum of n numbers among the previous p numbers
	'''
	l = len(arr)
	pre = arr[0:p]
	for i in range(p, l):
		if not isSum(arr[i], pre, 2):
			return arr[i]
		pre.pop(0)
		pre.append(arr[i])
	return -1

def getContiguousNumSet(n, arr):
	'''
	Returns an array of contiguous numbers from arr which sum is n
	'''
	numSet = []
	sum = 0
	start = 0
	end = start
	l = len(arr)
	while end < l:
		if sum > n:
			sum -= numSet[0]
			numSet.pop(0)
			start += 1
		elif sum == n and len(numSet) > 1:
			return numSet
		else:
			numSet.append(arr[end])
			sum += arr[end]
			end += 1
	return []
	
# main
	
file1 = open('input/input09.txt', 'r')
lines = file1.readlines()

arr = [int(l) for l in lines]

print("Part 1:")
v = getInconvenientValue(arr, 25, 2)
print(v)

print("Part 2:")
ss = getContiguousNumSet(v, arr)
ss.sort()
print(ss[0] + ss[-1])
	
file1.close()