import copy
import time

def get_seats(file):
	seats = []
	with open(file, 'r') as f:
		seats = f.read().split('\n')
	return [list(s) for s in seats]


def wrap(seats):
	wrapped = [['0' for i in range(len(seats[0]) + 2)] for j in range(len(seats) + 2)]
	for i in range(len(seats)):
		for j in range(len(seats[0])):
			wrapped[i+1][j+1] = seats[i][j]
	return wrapped


def part_one_round(wrapped_seats):
	seats = copy.deepcopy(wrapped_seats)
	for i in range(1, len(wrapped_seats)-1):
		for j in range(1, len(wrapped_seats[0])-1):
			if wrapped_seats[i][j] == 'L' and cnt_neighbours(wrapped_seats, (i, j)) == 0:
				seats[i][j] = '#'
			elif wrapped_seats[i][j] == '#' and cnt_neighbours(wrapped_seats, (i, j)) > 3:
				seats[i][j] = 'L'
	return seats


def part_two_round(wrapped_seats):
	seats = copy.deepcopy(wrapped_seats)
	for i in range(1, len(wrapped_seats)-1):
		for j in range(1, len(wrapped_seats[0])-1):
			if wrapped_seats[i][j] == 'L' and cnt_visible(wrapped_seats, (i, j)) == 0:
				seats[i][j] = '#'
			elif wrapped_seats[i][j] == '#' and cnt_visible(wrapped_seats, (i, j)) > 4:
				seats[i][j] = 'L'
	return seats 


def cnt_neighbours(seats, seat):
	cnt = 0
	x, y = seat

	if seats[x-1][y-1] == '#': cnt += 1
	if seats[x-1][y] == '#': cnt += 1
	if seats[x][y-1] == '#': cnt += 1
	if seats[x+1][y+1] == '#': cnt += 1
	if seats[x+1][y] == '#': cnt += 1
	if seats[x][y+1] == '#': cnt += 1
	if seats[x+1][y-1] == '#': cnt += 1
	if seats[x-1][y+1] == '#': cnt += 1

	return cnt


def cnt_visible(seats, seat):
	cnt = 0
	x, y = seat[0]+1, seat[1]
	while seats[x][y] != '0':
		if seats[x][y] == '#':
			cnt += 1
			break
		elif seats[x][y] == 'L': break
		else: x += 1

	x, y = seat[0], seat[1]+1
	while seats[x][y] != '0':
		if seats[x][y] == '#':
			cnt += 1
			break
		elif seats[x][y] == 'L': break
		else: y += 1

	x, y = seat[0]-1, seat[1]
	while seats[x][y] != '0':
		if seats[x][y] == '#':
			cnt += 1
			break
		elif seats[x][y] == 'L': break
		else: x -= 1

	x, y = seat[0], seat[1]-1
	while seats[x][y] != '0':
		if seats[x][y] == '#':
			cnt += 1
			break
		elif seats[x][y] == 'L': break
		else: y -= 1

	x, y = seat[0]+1, seat[1]+1
	while seats[x][y] != '0':
		if seats[x][y] == '#':
			cnt += 1
			break
		elif seats[x][y] == 'L': break
		else: 
			x += 1
			y += 1

	x, y = seat[0]-1, seat[1]-1
	while seats[x][y] != '0':
		if seats[x][y] == '#':
			cnt += 1
			break
		elif seats[x][y] == 'L': break
		else: 
			x -= 1
			y -= 1

	x, y = seat[0]-1, seat[1]+1
	while seats[x][y] != '0':
		if seats[x][y] == '#':
			cnt += 1
			break
		elif seats[x][y] == 'L': break
		else: 
			x -= 1
			y += 1

	x, y = seat[0]+1, seat[1]-1
	while seats[x][y] != '0':
		if seats[x][y] == '#':
			cnt += 1
			break
		elif seats[x][y] == 'L': break
		else: 
			x += 1
			y -= 1

	return cnt


def count_final(seats):
	cnt = 0
	for s in seats:
		cnt += ''.join(s).count('#') 
	return cnt



def main():

	test = get_seats('test.txt')
	today_ip = get_seats('day11.txt')
	wrapped = wrap(today_ip)

	# part 1
	start_part_one = time.time()
	current_round = copy.deepcopy(wrapped)
	next_round = part_one_round(wrapped)

	rn = 1
	while next_round != current_round:
		rn += 1
		current_round = copy.deepcopy(next_round)
		next_round = part_one_round(next_round)

	last_round = count_final(next_round)
	finish_part_one = time.time()
	print(f'Part one: {last_round} seats occupied after {rn} rounds')
	print(f'	Finished in {round(finish_part_one - start_part_one, 5)} seconds\n')

	# part 2
	start_part_two = time.time()
	current_round = copy.deepcopy(wrapped)
	next_round = part_two_round(wrapped)

	rn = 1
	while next_round != current_round:
		rn += 1
		current_round = copy.deepcopy(next_round)
		next_round = part_two_round(next_round)

	last_round = count_final(next_round)
	finish_part_two = time.time()
	print(f'Part two: {last_round} seats occupied after {rn} rounds')
	print(f'	Finished in {round(finish_part_two - start_part_two, 5)} seconds')



main()