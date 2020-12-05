
def get_input(file):
	data = []
	with open(file, 'r') as f:
		data = f.readlines()
	return [line.replace('\n', '') for line in data]

def find_id(seat):
	f, b = 0, 127
	l, up = 0, 7
	for c in seat:
		if c == 'F':
			b = (f+b)//2
		if c == 'B':
			f = (f+b)//2 + 1
		if c == 'L':
			up = (l+up)//2
		if c == 'R':
			l = (l+up)//2 + 1

	return f * 8 + l

def your_id(ids):
	for i in range(1, len(ids)):
		if ids[i] - ids[i-1] == 2:
			return ids[i]-1

def main():
	seats = get_input('day5.txt')
	ids = sorted([find_id(seat) for seat in seats])
	print(max(ids))
	print(your_id(ids))

if __name__ == '__main__':
	main()
