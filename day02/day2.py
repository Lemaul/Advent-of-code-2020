'''
02.12.2020 
Solution for advent of code day 2
part 1 was to check if number of given letter in a string is in specified range ()
Part 2 is about checking if given letter is in password[minimum-1] XOR in password[maximum-1],

Finishes in 0.004-0.006 seconds (including getting input and counting results)
'''

import time


def get_input(file):
	data = []
	with open(file, 'r') as f:
		data = f.readlines()

	for i, line in enumerate(data):
		dash_index = line.index('-')
		colon_index = line.index(':')
		data[i] = {'minimum' : int(line[0 : dash_index]), 
				   'maximum' : int(line[dash_index+1 : colon_index-2]),
				   'letter' : line[colon_index-1],
				   'password' : line[colon_index+2:len(line)-1]}
		
	return data

def check_password_part1(line):
	return line['minimum'] <= line['password'].count(line['letter']) <= line['maximum']

def check_password_part2(line):
	return (line['password'][line['minimum'] - 1] == line['letter']) ^ (line['password'][line['maximum'] - 1] == line['letter'])

def main():
	start_time = time.time()
	data = get_input('day2.txt')

	result_part1 = sum(check_password_part1(line) for line in data)
	print(result_part1)

	result_part2 = sum(check_password_part2(line) for line in data)
	print(result_part2)
	finish_time = time.time()
	print('Finished in: ' + str(round(finish_time - start_time, 5)) + ' seconds.')

main()
