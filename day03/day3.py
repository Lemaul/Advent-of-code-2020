'''
03.12.2020 
Solution for advent of code 2020 day 3
Today part 1 was to traverse input such that in each row you go 3 right and 1 down (count_trees)
For part 2 added parameters right and down to count_trees because of different traversions like 7 right 1 etc
The result for part 2 was to return the product of t1_1 (traversion of 1 right and 1 down), t3_1, t5_1, t7_1, t1_2
'''


def get_input(file):
	data = []
	with open(file, 'r') as f:
		data = f.readlines()
		
	return [data[i][:len(data[i])-1] for i in range(len(data))]

def count_trees(slope, right, down):
	trees = 0
	index = 0
	for i in range(0, len(slope), down):
		if slope[i][index] == '#': trees += 1
		index = index + right if index + right < len(slope[i]) else (index+right)%len(slope[i])
	return trees

def main():
	slope = get_input('day3.txt')
	
	t1_1 = count_trees(slope, 1, 1)
	t3_1 = count_trees(slope, 3, 1)
	t5_1 = count_trees(slope, 5, 1)
	t7_1 = count_trees(slope, 7, 1)
	t1_2 = count_trees(slope, 1, 2)
	print(str(t1_1*t3_1*t5_1*t7_1*t1_2))

main()