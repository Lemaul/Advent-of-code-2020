'''
01.12.2020
Solution for advent of code 2020 day 1
the task was to find the product of two(find_two) and three(find_three) numbers which sum is 2020
apparently find_two() and find_three() work faster than their square and cubed versions, 
which I added later to actually see if that's the case

solution with *in* takes 0.034-0.05 seconds
			   nested loops takes 0.6-0.638 seconds
'''

import time
from math import prod

def get_numbers(file):
	numbers = []
	with open(file, 'r') as f:
		numbers = f.readlines()

	return [int(n) for n in numbers]

def find_two(numbers, integer):
	for n in numbers:
		if (integer - n) in numbers:
			return (n, integer-n)

def find_three(numbers, integer):
	for n in numbers:
		if (find_two(numbers, integer-n)):
			return (n, find_two(numbers, integer-n)[0], find_two(numbers, integer-n)[1])

def square_find_two(numbers, integer):
	for i in range(len(numbers)):
		for j in range(len(numbers)):
			if numbers[i] + numbers[j] == integer:
				return (numbers[i], numbers[j])

def cube_find_three(numbers, integer):
	for i in range(len(numbers)):
		for j in range(len(numbers)):
			for k in range(len(numbers)):
				if numbers[i] + numbers[j] + numbers[k] == integer:
					return (numbers[i], numbers[j], numbers[k])

start_in = time.time()
two = find_two(get_numbers('day1.txt'), 2020)
three = find_three(get_numbers('day1.txt'), 2020)
end_in = time.time()

print('Two numbers and their product')
print(str(two) + ' ==> ' + str(prod(two)))
print('\nThree numbers and their product')
print(str(three) + ' ==> ' + str(prod(three)))
print('Solution with in took ' + str(round(end_in - start_in, 3)) + ' seconds.')

print('\nGET READY FOR QUADRATIC AND CUBIC TIME COMPLEXITY')
start_brutality = time.time()
square_two = square_find_two(get_numbers('day1.txt'), 2020)
cube_three = cube_find_three(get_numbers('day1.txt'), 2020)
end_brutality = time.time()

print('Two numbers and their product (brutal)')
print(str(square_two) + ' ==> ' + str(prod(square_two)))
print('\nThree numbers and their product (brutal af)')
print(str(cube_three) + ' ==> ' + str(prod(cube_three)))
print('Brutal solution took ' + str(round(end_brutality - start_brutality, 3)) + ' seconds.')
