
def get_instructions(file):
	instructions = []
	with open(file, 'r') as f:
		instructions = f.read().split('\n')
	return [(it[0], int(it[1:])) for it in instructions]


def part_one(instructions):

	def new_face(llist, n, face):
		while n > 0:
			face = llist[face]
			n -= 1
		return face

	dst = {'N': 0, 'E': 0, 'W': 0, 'S': 0}
	llistL = {'N': 'W', 'W': 'S', 'S': 'E', 'E': 'N'}
	llistR = {'N': 'E', 'E': 'S', 'S': 'W', 'W': 'N'}
	facing = 'E'
	for it in instructions:
		if it[0] in dst:
			dst[it[0]] += it[1]
		elif it[0] == 'F':
			dst[facing] += it[1]
		elif it[0] == 'L':
			facing = new_face(llistL, it[1]//90, facing)
		else:
			facing = new_face(llistR, it[1]//90, facing)

	return abs(dst['N'] - dst['S']) + abs(dst['E'] - dst['W'])


# def part_two(instructions):

# 	def rotate_wp():
# 		pass

# 	waypoint = {'N': 1, 'E': 10, 'W': 0, 'S': 0}
# 	dst = {'N': 0, 'E': 0, 'W': 0, 'S': 0}

# 	for it in instructions:
# 		if it

# 	return abs(dst['N'] - dst['S']) + abs(dst['E'] - dst['W'])


def main():
	test = 'test.txt'
	today_ip = 'day12.txt'
	instructions = get_instructions(test)
	
	dst = part_one(instructions)
	print(dst)


main()