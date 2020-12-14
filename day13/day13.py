
def get_buses(file):
	time = 0
	buses = None
	with open(file, 'r') as f:
		time = int(f.readline())
		buses = f.readline().split(',')
	return time, [int(b) if b != 'x' else b for b in buses]


def first_bus(time, buses):
	buses_wox = [b for b in buses if b != 'x']
	timetable = [time//b*b + b - time for b in buses_wox]
	return buses_wox[timetable.index(min(timetable))] * min(timetable), buses_wox[timetable.index(min(timetable))], min(timetable)


def timestamp(buses, test):
	buses_wox = [b for b in buses if b != 'x']
	t = buses[0] if test else 100000000000000//buses[0]*buses[0]
	departures = []
	for i in range(len(buses)):
		if buses[i] != 'x': departures.append(i)
	while True:
		correct = 0
		for bus, dep in zip(buses_wox, departures):
			if (t+dep)%bus == 0:
				correct += 1
		if correct == len(buses_wox): break
		t += buses[0]

	return t


def main():
	
	test = 'test.txt'
	todayip = 'day13.txt'
	time, buses = get_buses(test)

	part_one, bus, time_waiting = first_bus(time, buses)
	print(f'Bus {bus}, time to wait {time_waiting} minutes, {bus} * {time_waiting} = {part_one}')

	print(timestamp(buses, True))


main()