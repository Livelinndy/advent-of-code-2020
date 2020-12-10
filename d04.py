# Day 4: Passport Processing
# https://adventofcode.com/2020/day/4

from functools import reduce
import operator
import re

def getNbCorrectPassports_part1(lines):
	'''
	Returns the number of correct passwords
	For each passport we are checking the presence of necessary fields
	'''
	fields = { "byr": False, "iyr": False, "eyr": False, "hgt": False, "hcl": False, "ecl": False, "pid": False }
	count = 0
	for line in lines:
		if line == "\n":
			if reduce(operator.__and__, fields.values()):
				count += 1
			fields["byr"] = False
			fields["iyr"] = False
			fields["eyr"] = False
			fields["hgt"] = False
			fields["hcl"] = False
			fields["ecl"] = False
			fields["pid"] = False
		else:
			if "byr" in line: fields["byr"] = True
			if "iyr" in line: fields["iyr"] = True
			if "eyr" in line: fields["eyr"] = True
			if "hgt" in line: fields["hgt"] = True
			if "hcl" in line: fields["hcl"] = True
			if "ecl" in line: fields["ecl"] = True
			if "pid" in line: fields["pid"] = True
	if reduce(operator.__and__, fields.values()):
		count += 1
	return count

def getNbCorrectPassports_part2(lines):
	'''
	Returns the number of correct passwords
	For each passport we are checking not only the presence of necessary fields but also the validity of values
	'''
	fields = { "byr": False, "iyr": False, "eyr": False, "hgt": False, "hcl": False, "ecl": False, "pid": False }
	count = 0
	for line in lines:
		if line == "\n":
			if reduce(operator.__and__, fields.values()):
				count += 1
			fields["byr"] = False
			fields["iyr"] = False
			fields["eyr"] = False
			fields["hgt"] = False
			fields["hcl"] = False
			fields["ecl"] = False
			fields["pid"] = False
		else:
			line = line.strip()
			a = line.split(' ')
			for b in a:
				c = b.split(':')
				if c[0] == "byr":
					if re.match(r"^\d{4}$", c[1]):
						byrVal = int(c[1])
						if byrVal >= 1920 and byrVal <= 2002:
							fields["byr"] = True
				elif c[0] == "iyr":
					if re.match(r"^\d{4}$", c[1]):
						iyrVal =  int(c[1])
						if iyrVal >= 2010 and iyrVal <= 2020:
							fields["iyr"] = True
				elif c[0] == "eyr":
					if re.match(r"^\d{4}$", c[1]):
						eyrVal =  int(c[1])
						if eyrVal >= 2020 and eyrVal <= 2030:
							fields["eyr"] = True
				elif c[0] == "hgt":
					if re.match(r"^\d{2,3}(cm|in)$", c[1]):
						l = len(c[1])
						m = c[1][-2:]
						n = int(c[1][0:l-2])
						if m == "in":
							if n >= 59 and n <= 76:
								fields["hgt"] = True
						elif m == "cm":
							if n >= 150 and n <= 193:
								fields["hgt"] = True
				elif c[0] == "hcl":
					if re.match(r"^#[0-9a-f]{6}$", c[1]): fields["hcl"] = True
				elif c[0] == "ecl":
					posVal = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
					if c[1] in posVal:
						fields["ecl"] = True
				elif c[0] == "pid":
					if re.match(r"^\d{9}$", c[1]):
						fields["pid"] = True
	if reduce(operator.__and__, fields.values()):
		count += 1
	return count

# main
	
file1 = open('input/input04.txt', 'r')
lines = file1.readlines()

print("Part 1:")
print(getNbCorrectPassports_part1(lines))

print("Part 2:")
print(getNbCorrectPassports_part2(lines))

file1.close()