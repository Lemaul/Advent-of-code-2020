
import math

def get_nums(file):
	with open(file, 'r') as f:
		nums = f.read().split('\n')
		return [int(n) for n in nums]


def get_differences(numbers):
	numbers = sorted(numbers)
	diffs = {1: 0, 3: 1}
	diffs[numbers[0]] += 1
	for i in range(1, len(numbers)):
		diffs[numbers[i] - numbers[i-1]] += 1

	return diffs[3] * diffs[1], diffs[1], diffs[3]


def get_combinations(numbers):
	numbers = sorted(numbers)
	diffs = [0 for n in numbers]
	diffs[0] = numbers[0]
	ones_sequences = []
	current = 0 if numbers[0] == 3 else 1
	for i in range(1, len(numbers)):
		diffs[i] = numbers[i] - numbers[i-1]
		if diffs[i] == 1:
			current += 1
		elif diffs[i-1] != 3:
			ones_sequences.append(current)
			current = 0
	ones_sequences.append(current)

	result = 1
	for seq in ones_sequences:
		if seq == 4: result *= 7
		elif seq == 3: result *= 4
		elif seq == 2: result *= 2 
	return result



test = 'test.txt'
small_test = 'small_test.txt'
todays_input = 'day10.txt'

nums = get_nums(todays_input)

part_one, dif1, dif3 = get_differences(nums)

print(f'Differences of 1: {dif1} * differeces of 3: {dif3} = {part_one}')

differences = get_combinations(nums)
print(f'Different combinations: {differences}')