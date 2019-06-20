with open('input.txt') as file_object:
	scanners = file_object.readlines()

for i in range(0, len(scanners)):
	scanners[i].rstrip()
	scanners[i] = scanners[i].split(': ')
	scanners[i][0] = int(scanners[i][0])
	scanners[i][1] = int(scanners[i][1])

scanner_ranges = {}
for i in range(0, 91):
	scanner_ranges[i] = -1

for scanner in scanners:
	scanner_ranges[scanner[0]] = scanner[1]

def find_severity(delay):
	sev = 0
	for pos in range(0, 91):
		if(scanner_ranges[pos] != -1 and ((pos + delay) % (2 * (scanner_ranges[pos] - 1))) == 0):
			sev += pos * scanner_ranges[pos]
	return sev

def causes_collision(delay):
	for pos in range(0, 91):
		if(scanner_ranges[pos] != -1 and ((pos + delay) % (2 * (scanner_ranges[pos] - 1))) == 0):
			return True
	return False

print(find_severity(0))

to_continue = True
delay = 0

while to_continue:
	if (delay % 4 != 0 and not causes_collision(delay)):
		to_continue = False
		print(delay)
	else:
		delay += 1