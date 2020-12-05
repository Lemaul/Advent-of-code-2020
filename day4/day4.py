
def get_passports(file):
	fields = { 'byr' : False,
			   'iyr' : False,
			   'eyr' : False,
			   'hgt' : False,
			   'hcl' : False,
			   'ecl' : False,
			   'pid' : False,
			   'cid' : False }

	data = []
	with open(file, 'r') as f:
		data = f.readlines()

	passports = []
	tempdict = dict(fields)
	for i, line in enumerate(data):
		for field in tempdict: # looking for fields in tempdict
			if field in line:
				field_index = line.find(field)
				line_remainder = line[field_index + len(field) + 1:]
				field_content = line_remainder[:line_remainder.find(' ')]
				tempdict[field] = field_content
		if ':' not in line: # passport is over, restart values
			passports.append(tempdict)
			tempdict = dict(fields)

	passports.append(tempdict)
	return passports


def valid_fields(passport):
	for field in passport:
		if not passport[field] and field != 'cid':
			return False
	return True

def byr(x):
	return len(x) == 4 and 1920 <= int(x) <= 2002

def iyr(x):
	return len(x) == 4 and 2010 <= int(x) <= 2020

def eyr(x):
	return len(x) == 4 and 2020 <= int(x) <= 2030

def hgt(x):
	if 'cm' not in x and 'in' not in x: return False
	height = int(x[:len(x)-2])
	if 'cm' in x:
		return 150 <= height <= 193
	return 59 <= height <= 76

def hcl(x):
	if x[0] != '#': return False
	for c in x:
		if c not in '#0123456789abcdef': return False
	return True

def ecl(x):
	return x in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']

def pid(x):
	if len(x) != 9: return False
	for c in x:
		if c not in '0123456789': return False
	return True

def valid_data(passport):
	return valid_fields(passport) and byr(passport['byr']) and iyr(passport['iyr']) and eyr(passport['eyr']) and hgt(passport['hgt']) and hcl(passport['hcl']) and ecl(passport['ecl']) and pid(passport['pid'])


def main():
	passports = get_passports('day4.txt')
	cnt_valid_fields = 0
	cnt_valid_data = 0
	for passport in passports:
		if valid_fields(passport):
			cnt_valid_fields += 1
		if valid_data(passport):
			cnt_valid_data += 1
	print(cnt_valid_fields)
	print(cnt_valid_data)


if __name__ == '__main__':
	main()