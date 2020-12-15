
def get_numbers(file):
	with open(file, 'r') as f:
		return [int(n) for n in f.read().split(',')]


def find_number(nums, n):
	seq = list(nums)
	numbers = {}
	for i, s in enumerate(seq):
		numbers[s] = [i]

	for i in range(len(seq), n):
		if len(numbers[seq[-1]]) == 1: 
			seq.append(0)
			numbers[0].append(i)
		else: 
			seq.append(numbers[seq[-1]][-1] - numbers[seq[-1]][-2])
			if seq[-1] in numbers: numbers[seq[-1]].append(i)
			else: numbers[seq[-1]] = [i]

	return seq[-1]


def main():
	test = False
	nums = get_numbers('test.txt') if test else get_numbers('day15.txt')

	part_one = find_number(nums, 2020)
	part_two = find_number(nums, 30000000)
	print(f'2020th number: {part_one}')
	print(f'30000000th number: {part_two}')


main()
