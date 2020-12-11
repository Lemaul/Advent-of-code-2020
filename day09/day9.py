
def get_numbers(file):
	numbers = []
	with open(file, 'r') as f:
		numbers = f.read().split('\n')
	return [int(n) for n in numbers]


def find_first(numbers, test):
	preamble_len = 25
	if test: preamble_len = 5

	for i in range(preamble_len, len(numbers)):
		current = current_preamble(numbers, preamble_len, i - preamble_len)
		if numbers[i] not in current:
			return numbers[i]


def current_preamble(numbers, preamble_len, start_ind):
	sums = set()
	for i in range(start_ind, start_ind + preamble_len):
		for j in range(start_ind, start_ind + preamble_len):
			if i != j:
				sums.add(numbers[i] + numbers[j]) 
	return sums


def find_weakness(numbers, n, index):
	L, R = 0, 0
	current = 0

	while R < index:
		current = sum(numbers[L:R+1])
		if current == n:
			return min(numbers[L:R+1]) + max(numbers[L:R+1])
		elif current > n:
			L += 1
		else: R += 1



def main():
	test = False
	nums = get_numbers('day9.txt') if not test else get_numbers('test.txt')

	part_one = find_first(nums, test)

	index_one = nums.index(part_one)
	
	part_two = find_weakness(nums, part_one, index_one)
	
	print('First number without it\'s sum in preamble: ' + str(part_one))
	print('Sum of the smallest and biggest number of encryption weakness: ' + str(part_two))


main()