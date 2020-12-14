
def get_input(file):
	data = []
	with open(file, 'r') as f:
		data = f.read().split('\nma')
	data = [d.split('\n') for d in data]

	return data


def part_one(data):
	powers = [2**i for i in range(36)]
	powers.reverse()

	mem = {}
	decimal_sum = 0
	
	for d in data:
		mask = d[0][-36:]
		for it in d:
			if 'sk' not in it:
				key = it.split(' ')[0].replace('mem[', '').replace(']', '')
				value = dec_to_bin(int(it.split(' ')[2]))

				masked = mask_number(mask, value)
				mem[key] = masked
		
	for key in mem:
		decimal_sum += bin_to_dec(mem[key])

	return decimal_sum


# def part_two(data):

# 	for d in data:
# 		mask = d[0][-36:]
# 		for it in d:
# 			if 'sk' not in it:
# 				memory = it.split(' ')[0].replace('mem[', '').replace(']', '')
# 				value = dec_to_bin(int(it.split(' ')[2]))

# 				masked = mask_memory(mask, memory)
# 				mem[key] = masked


def mask_number(mask, value):
	mask = list(mask)
	value = list(value)
	masked = []
	for cm, cv in zip(mask, value):
		if cm != 'X':
			masked.append(cm)
		else: masked.append(cv)
	return ''.join(masked)


def mask_memory(mask, value):
	mask = list(mask)
	value = list(value)
	masked = []
	for cm, cv in zip(mask, value):
		if cm == 'X' or cm == '1':
			masked.append(cm)
		else: masked.append(cv)
	return ''.join(masked)


def dec_to_bin(n):
	return '0'*(36-(len(bin(n))-2)) + bin(n)[2:]
	

def bin_to_dec(n):
	power = 34359738368
	dec = 0
	for c in n:
		if c == '1':
			dec += power
		power //= 2
	return dec


def main():
	test = False
	data = get_input('test.txt') if test else get_input('day14.txt')

	print(part_one(data))


main()

