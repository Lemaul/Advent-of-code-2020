import copy

def get_input(file):
	instructions = []
	with open(file, 'r') as f:
		instructions = f.read().split('\n')
	return [[i[:3], int(i[i.find(' '):])] for i in instructions]


def part_one(inst):
	visited = [False for instruction in inst]
	
	acc = 0
	index = 0
	while True:
		if visited[index] == True: return acc
		if inst[index][0] == 'nop':
			visited[index] = True
			index += 1
		elif inst[index][0] == 'acc':
			visited[index] = True
			acc += inst[index][1]
			index += 1
		else:
			visited[index] = True
			index += inst[index][1]


def part_two(inst):
	visited = [False for instruction in inst]
	for i, ins in enumerate(inst):
		if ins[0] == 'jmp':
			next_inst = copy.deepcopy(inst)
			next_inst[i][0] = 'nop'
			value = check(next_inst)
			if not isinstance(value, bool):
				return value


def check(inst):
	visited = [False for instruction in inst]
	acc = 0
	index = 0
	while True:
		if index == len(inst)-1:
			if inst[index][0] == 'acc':
				return acc + inst[index][1] 
			return acc
		if visited[index] == True: return False
		if inst[index][0] == 'nop':
			visited[index] = True
			index += 1
		elif inst[index][0] == 'acc':
			visited[index] = True
			acc += inst[index][1]
			index += 1
		else:
			visited[index] = True
			index += inst[index][1]
		

def main():
	instructions = get_input('day8.txt')
	acc = part_one(instructions)
	acc2 = part_two(instructions)
	
	print(acc)
	print(acc2)



if __name__ == '__main__':
	main()