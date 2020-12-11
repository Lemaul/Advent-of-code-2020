
def get_input(file):
	data = []
	with open(file, 'r') as f:
		data = f.read().split('\n\n')
	return [group.split('\n') for group in data]

def part_one(answers):
	yes = []
	for group in answers:
		temp = set()
		for person in group:
			for c in person:
				temp.add(c)
		yes.append(temp)
	return sum(len(g) for g in yes)

def part_two(answers):
	result = 0
	for group in answers:
		temp = []
		occurences = set()
		for person in group:
			for c in person:
				temp.append(c)
				occurences.add(c)
		for c in occurences:
			if temp.count(c) == len(group):
				result += 1
	return result


def main():
	groups = get_input('day6.txt')
	print(part_one(groups))
	print(part_two(groups))


if __name__ == '__main__':
	main()