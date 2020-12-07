# Day 7: Handy Haversacks
# https://adventofcode.com/2020/day/7

def getBags(lines):
	bags = {}
	for line in lines:
		a = line.split(' ')
		b = a[0] + " " + a[1]
		l = len(a)
		if l == 7:
			bags[b] = None
		else:
			i = 4
			bags[b] = {}
			while i < l:
				n = int(a[i])
				c = a[i+1] + " " + a[i+2]
				bags[b][c] = n
				i += 4
	return bags

def getNbOutermostBags(bag, allBags, allOuterBags):
	currentOuterBags = []
	res = 0
	for key, value in allBags.items():
		if value is not None:
			if bag in value:
				if key not in allOuterBags:
					currentOuterBags.append(key)
					res += 1
	allOuterBags += currentOuterBags
	for outerBag in currentOuterBags:
		res += getNbOutermostBags(outerBag, allBags, allOuterBags)
	return res

def getNbInnerBags(bag, allBags):
	if bag in allBags:
		if allBags[bag] is not None:
			res = 0
			for key, value in allBags[bag].items():
				res += value + (value * getNbInnerBags(key, allBags))
			return res
		return 0
	return 0
	
# main
	
file1 = open('input/input7.txt', 'r')
lines = file1.readlines()

bags = getBags(lines)

print("Part 1:")
print(getNbOutermostBags("shiny gold", bags, []))

print("Part 2:")
print(getNbInnerBags("shiny gold", bags))

file1.close()