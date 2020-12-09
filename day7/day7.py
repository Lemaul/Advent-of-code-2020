
def get_input(file):
	rules = {}
	with open(file, 'r') as f:
		data = f.read().split('.\n')
		for color in data:
			ind_bags = color.find('bags')
			ind_contain = color.find('contain')
			current_key = color[:ind_bags-1]
			value = color[ind_contain + len('contain')+1:].replace('bags', '').replace('bag', '').replace('.', '')
			rules[current_key] = value.split(', ')

			new_rule = []
			for rule in rules[current_key]:
				if 'no other' not in rule:
					new_rule.append((rule[2:-1], int(rule[0])))
				
			rules[current_key] = new_rule

	return rules

def part_one(rules, visited, golden):
	visited = set()
 
	for rule in rules:
		DFS(rules, rule, visited, golden)

	for rule in rules:
		for color in rules[rule]:
			if color[0] in golden:
				golden.add(rule)
	return golden

def DFS(rules, rule, visited, golden):
	visited.add(rule)
	# print(rule, end='\n')
	for color in rules[rule]:
		if color[0] == 'shiny gold' or color[0] in golden:
			golden.add(rule)
		if color[0] not in visited:
			DFS(rules, color[0], visited, golden)
			


def main():
	rules = get_input('day7.txt')

	golden_bag = {rule: False for rule in rules}
	visited = set()
	golden = set()
	szmozo = part_one(rules, visited, golden)
	print(len(szmozo))
	

if __name__ == '__main__':
	main()