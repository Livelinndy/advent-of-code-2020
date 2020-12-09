# Day 9: Encoding Error
# https://adventofcode.com/2020/day/9

from itertools import combinations
from functools import reduce
import operator

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
	ss = []
	s = 0
	j = 0
	i = j
	l = len(arr)
	while i < l:
		if s > n:
			ss = []
			s = 0
			j += 1
			i = j
		elif s == n and len(ss) > 1:
			return ss
		else:
			ss.append(arr[i])
			s += arr[i]
			i += 1
	return []
	
# main
	
file1 = open('input/input9.txt', 'r')
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